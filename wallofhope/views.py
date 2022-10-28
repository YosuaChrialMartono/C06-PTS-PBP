from django.shortcuts import render
from wallofhope.models import wallofhope
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .forms import DataForm

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


def add_form_ajax(request):
    form = DataForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResposenseRedirect("wallofhope.html")

# def delete_card(request, id):
#     task = wallofhope.objects.get(id=id)
#     task.delete()
#     return redirect('wallofhope:show_wallofhope')

#def get_remote_image(self):
   # if self.image_url and not self.image_file:
        #result = urllib.urlretrieve(self.image_url)
        #self.image_file.save(
            #    os.path.basename(self.image_url),
              #  File(open(result[0]))
                #)
        #self.save()