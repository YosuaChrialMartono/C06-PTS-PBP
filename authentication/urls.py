from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login, logout, register
from django.views.decorators.csrf import csrf_exempt

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login_page'),
    path('logout/', logout, name='logout_page'),
    path('register/', register, name='register_page'),
]
