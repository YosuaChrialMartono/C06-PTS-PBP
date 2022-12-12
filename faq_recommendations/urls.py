from django.urls import path
from faq_recommendations.views import show_faq, show_json, add_exp 
app_name = 'faqs'

urlpatterns = [
    path('', show_faq, name='show_faq'),
<<<<<<< HEAD
    path('json/', show_json, name='show_json'),
    path('post-exp/', add_exp, name='add_exp'),
]
=======
    path('json/', show_json, name='show_json'),]
>>>>>>> fa8695016f3fd530a9dc49d2c42bc535f3dd093d
