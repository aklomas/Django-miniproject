from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView, View, FormView
from django.core.urlresolvers import reverse

import requests
import json
import pdb
import time


from .forms import UploadImageForm, SearchImageForm
from .models import Image

# nbar tells the menu on which page we are currently positioned. Please check base_top_menu.html.
#

UPLOAD_IMAGE_URL = "http://194.249.0.47:8080/CcgMiniV01/mini/images/uploadImage"
DELETE_IMAGE_URL = "http://194.249.0.47:8080/CcgMiniV01/mini/images/deleteSpecifiedImages"
GET_IMAGE_URL = "http://194.249.0.47:8080/CcgMiniV01/mini/images/returnSpecifiedImages"
GET_ALL_IMAGES_URL = "http://194.249.0.47:8080/CcgMiniV01/mini/images"


def deleteImage(request):
    if request.method == 'POST':
        if(request.POST.get('image_id')):  # If we get a correct delete POST requeste we proceed with deletion of the local files and form the database.
            data = "[\"{}\"]".format(request.POST['image_id'])
            headers = {'Content-type': 'application/json'}
            r = requests.post(DELETE_IMAGE_URL, data=data, headers=headers)
            Image.objects.filter(image_id=request.POST['image_id']).delete()
            return JsonResponse(r.json(), safe=False)
    else:
        return redirect(reverse('show_image'))


class Home(TemplateView):
    template_name = 'use_cases/index.html'
    nbar = 'home'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['nbar'] = self.nbar
        return context


class Show_image(FormView):
    initial = {}
    nbar = 'show_image'
    template_name = 'use_cases/show_image.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'nbar': self.nbar})

    def post(self, request, *args, **kwargs):
        if(request.POST.get('image_ids')):  # Check if the POST requeste wants us to show all or just specific images and serve appropriately.
            data = json.dumps(request.POST['image_ids'].split())
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r = requests.post(GET_IMAGE_URL, data=data, headers=headers)
            # pdb.set_trace()
            return JsonResponse(r.json(), safe=False)
        if(request.POST.get('is_all')):
            headers = {'Accept': 'application/json'}
            r = requests.get(GET_ALL_IMAGES_URL, headers=headers)
            return JsonResponse(r.json(), safe=False)


class Search_image(FormView):
    form_class = SearchImageForm
    initial = {}
    nbar = 'search_image'
    template_name = 'use_cases/search_image.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'nbar': self.nbar})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            url = "http://194.249.0.47:8080/CcgMiniV01/mini/images/returnImagesWithGivenType"
            data = "\"{}\"".format(request.POST['di_type'])
            headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
            r = requests.post(url, data=data, headers=headers)
            # pdb.set_trace()
            return JsonResponse(r.json(), safe=False)
        return render(request, self.template_name, {'form': form, 'nbar': self.nbar})


class Upload_image(View):
    form_class = UploadImageForm
    initial = {}
    nbar = 'upload_image'
    template_name = 'use_cases/upload_image.html'

    def uploadImage(request):
        uploaded_image = Image(pic=request.FILES['di_picture'],
                               DI=request.FILES['di_imagefile'])
        # JSON string below which will be sent to server as an upload request.
        data = "{{\"description\": \"{0}\", \"title\": \"{1}\", \"iri\": \"../media/uploads/diskimages/{1}\", \"imageType\": \"{2}\", \"fileFormat\": \"{3}\", \"pictureUrl\": \"../media/uploads/images/{4}\", \"encription\": {5}, \"needsData\": {6}, \"obfuscation\": {7}, \"price\": {8}, \"slaId\": {9}, \"operatingSystemId\": {10}, \"ownerId\": 66, \"predecessor\": \"predecessor of image {11}\", \"functionallityId\": 77, \"qualityId\": 88, \"generationTime\": {12} }}"
        data = data.format(request.POST['di_description'],
                           request.FILES['di_imagefile'].name,
                           request.POST['di_type'],
                           request.POST['di_fileformat'],
                           request.FILES['di_picture'].name,
                           "true" if request.POST.get('di_encription') else "false",
                           "true" if request.POST.get('di_needsdatafile') else "false",
                           "true" if request.POST.get('di_obfuscation') else "false",
                           request.POST['di_price'],
                           request.POST['di_SLA'],
                           request.POST['di_operatingsystem'],
                           request.FILES['di_imagefile'].name,
                           int(round(time.time())))
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(UPLOAD_IMAGE_URL, data=data, headers=headers)
        # TODO: Response check
        uploaded_image.image_id = r.json().get('id')
        uploaded_image.save()
        return r.json()

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'nbar': self.nbar})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return JsonResponse(self.uploadImage(request), safe=False)
        return render(request, self.template_name, {'form': form, 'nbar': self.nbar})
