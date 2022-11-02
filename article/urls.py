from django.urls import path
from article.views import show_article_by_page, show_main_page, show_json, show_json_by_page, register, login, logout, post_article

app_name = 'article'

urlpatterns = [
    path('', show_main_page, name='show_main_page'),
    path('post-article/', post_article, name='post_article'),
    path('articles/<str:id>/', show_article_by_page, name='show_article_by_page'),
    path('json/', show_json, name='show_json'),
    path('json/<int:page_num>', show_json_by_page, name='show_json_by_page'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]