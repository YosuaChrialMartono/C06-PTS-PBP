from django.shortcuts import render
from wallofhope.models import wallofhope
from wallofhope.forms import wallofhope
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .forms import DataForm
from django.shortcuts import redirect
import datetime 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


def show_wallofhope(request):
    data_user = wallofhope.objects.all()
    form = DataForm 

    if request.user.username == '':
        role = "PENGUNJUNG"
    else:
        role = request.user.role

    context = {
        'wallofhope_data': data_user,
        'form' : form,
        'role' : role
    }
    return render(request, "wallofhope.html", context)

def show_json(request):
    data = wallofhope.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def show_wallofhope_base(request):
    data_user = wallofhope.objects.all()
    form = DataForm 
    context = {
        'wallofhope_data': data_user,
        'form' : form
    }
    return render(request, "wallofhope.html", context)


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def petunjuk(request):
    data_user = wallofhope.objects.all()
    form = DataForm 
    context = {
        'wallofhope_data': data_user,
        'form' : form
    }
    return render(request, "petunjuk.html", context)


@csrf_exempt
def post_wallofhope_flutter(request):
    if (request.method == 'POST'):
        form = DataForm(request.POST or None)
        if form.is_valid():
            wallofhope_form = form.save(commit=False)
            wallofhope_form.fields.user = request.user.username
            wallofhope_form.save()
            return JsonResponse({
              "status": True,
              "message": "Berhasil post wall of hope",
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    return JsonResponse({
              "status": False,
              "message": form.errors,
              # Insert any extra data if you want to pass data to Flutter
            }, status=401)


