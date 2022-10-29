from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import json
from .forms import RegistrationForm

def signup(request):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("<h3>Anda sudah masuk ke akun dengan email " + str(user.email) + "</h3>")

	context = {}
	if request.POST and request.is_ajax:
		form = RegistrationForm(request.POST)
		data = {}
		if form.is_valid():
			form.save()
			data['success'] = True
			return HttpResponse(json.dumps(data), content_type='application/json')
		else:
			data['error'] = form.errors
			data['success'] = False
			context['registration_form'] = form
			return HttpResponse(json.dumps(data), content_type='application/json')

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'signup.html', context)

