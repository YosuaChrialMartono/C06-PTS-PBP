from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Data
from .forms import TrackingForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers


# Create your views here.
def show_index(request):
    form = TrackingForm
    if request.method == "POST":
        trackingForm = TrackingForm(request.POST)
        if trackingForm.is_valid():
            trackingForm.save()
            return redirect('redirect/')
    return render(request, "tracking.html",{'form':form})

def redirecting_page(request):
    return render(request, "redirect.html")

#@loginasadmin
def show_json(request):
    data = Data.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def validate_email(request):
    if request.is_ajax and request.method == "GET":
        # get the email from the client side.
        email = request.GET.get("email", None)
        # check for the email in the database.
        if Data.objects.filter(email = email).exists():
            # if email found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if email not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)