from django.shortcuts import render
from django.http import HttpResponse
from faq_recommendations.models import FreqAskedQuestions


# Create your views here.
def show_faq(request):
    data_faq = FreqAskedQuestions.objects.all()
    context = {
        'faq' : data_faq,
    }
    return render(request, 'freqaskedquestions.html', context)
