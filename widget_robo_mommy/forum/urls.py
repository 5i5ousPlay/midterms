from django.urls import path
from .views import *

urlpatterns = [
    path('forum/', forum_post_list_view, name='forum_post_list_view'),
    path('forum/forumposts/<int:pk>/details/', ForumPostDetailView.as_view(), name='forumpostdetailview'),
    path('forum/forumposts/add/', ForumPostCreateView.as_view(), name='forumpostcreateview'),
    path('forum/forumposts/<int:pk>/edit/', ForumPostUpdateView.as_view(), name='forumpostupdateview'),
]

app_name = 'forum'
