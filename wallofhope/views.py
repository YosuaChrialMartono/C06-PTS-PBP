from django.shortcuts import render
from wallofhope.models import wallofhope
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .forms import DataForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
import datetime 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def show_wallofhope(request):
    data_user = wallofhope.objects.all()
    form = DataForm 
    context = {
        'wallofhope_data': data_user,
        'form' : form
    }
    return render(request, "wallofhope.html", context)

def show_json(request):
    data = wallofhope.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/wallofhope/login/')
def add_form_ajax(request):
    form = DataForm(request.POST)
    if(form.is_valid() and request.method == 'POST'):
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi') 
        image = request.POST.get('image') 
        new_task = wallofhope(judul = judul, deskripsi = deskripsi, image = image)
        new_task.save()  
        return JsonResponse({
            'judul' : judul,
            'deskripsi' : deskripsi,
            'image' : image
        })
    else:
        messages.success(request, 'Tidak bisa menambahkan form tidak valid')

@login_required(login_url='/wallofhope/login/')
def petunjuk(request):
    data_user = wallofhope.objects.all()
    form = DataForm 
    context = {
        'wallofhope_data': data_user,
        'form' : form
    }
    return render(request, "petunjuk.html", context)




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            response = HttpResponseRedirect(reverse("wallofhope:show_wallofhope"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_wallofhope.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("wallofhope:login"))
    response.delete_cookie('last_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wallofhope:login')

    context = {'form': form}
    return render(request, 'register_wallofhope.html', context)


@login_required(login_url='/wallofhope/login/')
def delete_card(request, id):
    task = wallofhope.objects.get(id=id)
    task.delete()
    return redirect('wallofhope:show_wallofhope')
