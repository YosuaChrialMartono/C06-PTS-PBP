from django.urls import path
from tracking.views import show_index

app_name = 'tracking'

urlpatterns = [
    path('', show_index, name='show_index'),
]