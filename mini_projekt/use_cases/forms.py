from django import forms


class UploadImageForm(forms.Form):
    DI_TYPE = (("VMI", "Virtual machine Image"),
               ("CI", "Container Image"))
    DI_FORMAT = (("ISO", "ISO"),
                 ("DMG", "DMG"),
                 ("FVD", "FVD"),
                 ("IMG", "IMG"),
                 ("NDIF", "NDIF"),
                 ("QCOW", "QCOW"),
                 ("UDIF", "UDIF"),
                 ("VID", "VDI"),
                 ("VHD", "VHD"),
                 ("VMDK", "VMDK"),
                 ("WIM", "WIM"))
    DI_OS = (("10", "Windows"),
             ("20", "Linux"),
             ("30", "Macintosh"))
    DI_SLA = (("1", "Special SLA"),
              ("2", "Generic SLA"))

    di_type = forms.ChoiceField(label='Disk image type:',
                                widget=forms.Select,
                                choices=DI_TYPE,
                                error_messages={'required': 'Type is Required'})
    di_type.widget.attrs['name'] = 'Disk image type'
    di_type.widget.attrs['class'] = 'ui fluid dropdown'
    di_version = forms.CharField(label='Disk image version:',
                                 error_messages={'required': 'Version is Required'})
    di_fileformat = forms.ChoiceField(label='Disk image format:',
                                      widget=forms.Select,
                                      choices=DI_FORMAT,
                                      error_messages={'required': 'File format is Required'})
    di_fileformat.widget.attrs['name'] = 'Disk image format'
    di_fileformat.widget.attrs['class'] = 'ui fluid dropdown'
    di_description = forms.CharField(label='Descritpion of the image.',
                                     error_messages={'required': 'Description is Required'},
                                     widget=forms.Textarea(attrs={'rows': 10,
                                                                  'cols': 65,
                                                                  'placeholder': 'Here you can describe the content of the image in details. It will be used for search.'}))
    di_picture = forms.FileField(error_messages={'required': 'Picture is Required'})
    di_picture.widget.attrs['style'] = 'display: none;'
    di_encription = forms.BooleanField(label='Do you want your disk image to be encripted?',
                                       required=False,
                                       error_messages={'required': 'Encription is Required'})
    di_SLA = forms.ChoiceField(label='Disk image SLA:',
                               widget=forms.Select,
                               choices=DI_SLA,
                               error_messages={'required': 'SLA is Required'})
    di_SLA.widget.attrs['name'] = 'Disk image SLA'
    di_SLA.widget.attrs['class'] = 'ui fluid dropdown'
    di_price = forms.CharField(label='Price of disk image:',
                               error_messages={'required': 'Price is Required'})
    di_operatingsystem = forms.ChoiceField(label='OS running on the disk image:',
                                           widget=forms.Select,
                                           choices=DI_OS,
                                           error_messages={'required': 'OS is Required'})
    di_operatingsystem.widget.attrs['name'] = 'Disk image OS'
    di_operatingsystem.widget.attrs['class'] = 'ui fluid dropdown'
    di_needsdatafile = forms.BooleanField(label='Does your image need data file?',
                                          required=False,
                                          error_messages={'required': 'Data File is Required'})
    di_obfuscation = forms.BooleanField(label='Is your image obfuscated?',
                                        required=False,
                                        error_messages={'required': 'Obfuscated is Required'})
    di_imagefile = forms.FileField(label='Choose disk image file below:',
                                   error_messages={'required': 'ImageFile is Required'})
    di_imagefile.widget.attrs['style'] = 'display: none;'


class SearchImageForm(forms.Form):
    DI_TYPE = (("VMI", "Virtual machine Image"),
               ("CI", "Container Image"))
    DI_FORMAT = (("ISO", "ISO"),
                 ("DMG", "DMG"),
                 ("FVD", "FVD"),
                 ("IMG", "IMG"),
                 ("NDIF", "NDIF"),
                 ("QCOW", "QCOW"),
                 ("UDIF", "UDIF"),
                 ("VID", "VDI"),
                 ("VHD", "VHD"),
                 ("VMDK", "VMDK"),
                 ("WIM", "WIM"))
    DI_OS = (("10", "Windows"),
             ("20", "Linux"),
             ("30", "Macintosh"))
    DI_SLA = (("1", "Special SLA"),
              ("2", "Generic SLA"))

    di_type = forms.ChoiceField(label='Search by disk image type:',
                                widget=forms.Select,
                                choices=DI_TYPE,
                                error_messages={'required': 'Type is Required'})
    di_type.widget.attrs['class'] = 'ui fluid dropdown'

