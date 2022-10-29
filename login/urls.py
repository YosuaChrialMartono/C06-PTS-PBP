from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', signup, name='signup'),
]
