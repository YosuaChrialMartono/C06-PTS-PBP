from django.urls import path
from forum.views import show_forum, show_forum_json, detailed_forum, detailed_forum_json, get_user_json, create_thread, create_comment, get_child_comment, increment_replies, delete_comment, decrement_replies
from forum.views import login_user, logout_user, register_user

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('json/', show_forum_json, name='show_forum_json'),
    path('create/', create_thread, name='create_thread'),
    path('comment/', create_comment, name='create_comment'),
    path('delete-comment/', delete_comment, name='delete_comment'),
    path('increment_replies/', increment_replies, name='increment_replies'),
    path('decrement_replies/', decrement_replies, name='decrement_replies'),
    path('child_comment/', get_child_comment, name='gget_child_comment'),
    path('user/<int:id>/json/', get_user_json, name='get_user_json'),
    path('detailed/<int:id>/', detailed_forum, name='detailed_forum'),
    path('detailed/<int:id>/json/', detailed_forum_json, name='detailed_forum_json'),
    path('login/', login_user, name='login_user'),
    path('logout', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user')
]
