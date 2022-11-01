from django.shortcuts import render
from django.contrib import messages
from .models import Data
from .forms import TrackingForm

# Create your views here.
def show_index(request):
    form = TrackingForm
    if request.method == "POST":
        trackingForm = TrackingForm(request.POST)
        if trackingForm.is_valid():
            trackingForm.save()
            messages.success(request, 'Data berhasil disubmit')
    return render(request, "tracking.html",{'form':form})