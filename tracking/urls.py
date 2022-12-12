from django.urls import path
from tracking.views import show_index, show_json, validate_email, redirecting_page, post_tracker

app_name = 'tracking'

urlpatterns = [
    path('', show_index, name='show_index'),
    path('json/', show_json, name='show_json'),
    path('get/ajax/validate/nickname', validate_email, name='validate_email'),
    path('redirect/', redirecting_page, name='redirecting_page'),
    path('post-tracker/', post_tracker, name= 'post_tracker')
]