from django.shortcuts import render
from wallofhope.models import wallofhope
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .forms import DataForm
from django.shortcuts import redirect
import datetime 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
User = settings.AUTH_USER_MODEL

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



@login_required(login_url='/login/')
def delete_card(request, id):
    task = wallofhope.objects.get(id=id)
    task.delete()
    return redirect('wallofhope:show_wallofhope')
