from django.forms import ModelForm
from .models import Data

class TrackingForm(ModelForm):
    class Meta:
        model= Data
        fields='__all__'