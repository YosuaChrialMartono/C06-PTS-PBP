from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login, logout, register, show_user_json, show_user_json_id

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login_page'),
    path('logout/', logout, name='logout_page'),
    path('register/', register, name='register_page'),
    path('show-user-json', show_user_json, name="show_user_json"),
    path('show-user-json-id/<int:id>', show_user_json_id, name="show_user_json_id"),
]
