from django import forms

from .models import File_


class FileForm(forms.ModelForm):
    class Meta:
        model = File_
        fields = ('file',)
