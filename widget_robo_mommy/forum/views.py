from django.shortcuts import render
from django.views import generic
from .models import ForumPost, Reply

# Create your views here.
class ForumPostListView(generic.ListView):
    model = ForumPost
    template_name = 'forum/forumpost_list.html'
    queryset = ForumPost.objects.all()
    context_object_name = 'forumposts'
