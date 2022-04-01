from django import forms
from .models import DataUpload


class DataUploadForm(forms.ModelForm):
    class Meta:
        model = DataUpload
        fields = '__all__'