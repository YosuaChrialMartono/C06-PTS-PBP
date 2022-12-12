from django.urls import path
from faq_recommendations.views import show_faq
from faq_recommendations.views import show_json
app_name = 'faqs'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('/json', show_json, name='show_json'),
]