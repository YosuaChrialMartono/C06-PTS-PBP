from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from login.forms import RegistrationForm, UserAuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login.models import User
from django.http import HttpResponse
from django.core import serializers

@csrf_exempt
def login(request):
    print(request)
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!",
              "username": request.user.username,
              "role": request.user.role,
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return JsonResponse({
              "status": True,
              "message": "Berhasil mendaftar",
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    print(form.errors)
    return JsonResponse({
              "status": False,
              "message": form.errors,
              # Insert any extra data if you want to pass data to Flutter
            }, status=401)

@csrf_exempt         
def logout(request):
    logout(request)
    return JsonResponse({
            "status": True,
            "message": "Successfully Logged Out!"
            }, status=200)

def show_user_json(request):
  user = User.objects.all()

  return HttpResponse(serializers.serialize("json", user),content_type="application/json")

def show_user_json_id(request,id):
  user = User.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("json", user),content_type="application/json")