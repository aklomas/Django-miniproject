from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name="index"),
    url(r'^upload_image/$', views.Upload_image.as_view(), name='upload_image'),
    url(r'^search_image/$', views.Search_image.as_view(), name='search_image'),
    url(r'^show_image/$', views.Show_image.as_view(), name='show_image'),
    url(r'^delete/$', views.deleteImage, name='delete_image'),
]
