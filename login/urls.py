from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, login_page, landing_page
from django.views.decorators.csrf import csrf_exempt

app_name = 'login'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_page, name='login_page'),
    path('signup/', signup, name='signup'),
]
