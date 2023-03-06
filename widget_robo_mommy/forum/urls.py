from django.urls import path
from .views import *

urlpatterns = [
    path('forum/', forum_post_list_view, name='forum_post_list_view')
]
