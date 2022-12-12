from django import forms
from django.forms import ModelForm
from .models import Experiences

class ExpForm(ModelForm):
    class Meta:
        model = Experiences
        fields = ('nama', 'email', 'nomorHP', 'message')
        label = {
            'nama' : 'nama',
            'email' : 'email',
            'nomorHP' : 'nomorHP',
            'message' : 'message',
        }
        widgets = {
            'nama' : forms.TextInput(),
            'email' : forms.TextInput(),
            'nomorHP' : forms.TextInput(),
            'message' : forms.TextInput(),
        }