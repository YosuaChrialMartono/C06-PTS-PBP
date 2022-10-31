from django import forms
from django.forms import ModelForm
from .models import wallofhope


class DataForm(ModelForm):
    class Meta:
        model = wallofhope
        fields = ('judul', 'image', 'deskripsi')
        label = {
            'judul' : 'judul',
            'deskripsi' : 'deskripsi',
            'image' : 'Link image'
        }
        widgets = {
            'judul' : forms.TextInput(attrs={'type' : 'text', 'class' :'form-control', 'id':'input_title'}),
            'deskripsi' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control', 'id':'input_desc'}),
            'image' : forms.TextInput(attrs={'type': 'text', 'class' : "form-control", 'id' : 'input_image'})
        }
