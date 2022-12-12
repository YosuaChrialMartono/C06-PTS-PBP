from django.urls import path
from faq_recommendations.views import show_faq, show_json, add_exp 
app_name = 'faqs'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('json/', show_json, name='show_json'),
    path('post-exp/', add_exp, name='add_exp'),
]
