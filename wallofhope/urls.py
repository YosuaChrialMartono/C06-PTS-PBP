from django.urls import path
from wallofhope.views import login_user, logout_user
from wallofhope.views import show_wallofhope
from wallofhope.views import show_json
from wallofhope.views import add_form_ajax
from wallofhope.views import petunjuk
from wallofhope.views import delete_card
from wallofhope.views import show_wallofhope_guest

app_name = 'wallofhope'

urlpatterns = [
    path('', show_wallofhope, name='show_wallofhope'),
    path('json/', show_json, name='show_json'),
    path('add/' , add_form_ajax, name='add_form_ajax'), 
    path('petunjuk/', petunjuk, name='petunjuk'),
    path('delete/<int:id>', delete_card, name='delete_card'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),

    # path('a', show_wallofhope_guest, name= 'show_wallofhope_guest')

    
]
    
