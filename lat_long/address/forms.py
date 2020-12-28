
from django import forms
from .models import AddressFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = AddressFile
        fields = '__all__'
