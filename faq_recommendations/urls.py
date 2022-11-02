from django.urls import path
from faq_recommendations.views import show_faq
app_name = 'faqs'

urlpatterns = [
    path('', show_faq, name='show_faq'),
]