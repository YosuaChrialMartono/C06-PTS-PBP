from django.shortcuts import render
from django.http import HttpResponse
from faq_recommendations.models import FreqAskedQuestions
from django.core import serializers


# Create your views here.
def show_faq(request):
    data_faq = FreqAskedQuestions.objects.all()    
    context = {
        'faq' : data_faq,
    }
    return render(request, 'freqaskedquestions.html', context)

def show_json(request):
    data = FreqAskedQuestions.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")