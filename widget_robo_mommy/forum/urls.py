from django.urls import path
from .views import *

urlpatterns = [
    path('forum/', ForumPostListView.as_view())
]