from django import forms
from carapp.models import PicUpload

class ImageForm(forms.Form): #As this is not a ModelForm thats why we are not using forms.ModelForm
    imagefile = forms.ImageField(label='Select an image to upload')
