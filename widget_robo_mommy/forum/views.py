from django.shortcuts import render
from django.views import generic
from .models import ForumPost
import pytz
from django.utils import timezone


# helper function to convert utc datetime object to local time
def convert_utc_to_local(utctime, format):
    datetime_format = format
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(datetime_format)


def forum_post_list_view(request):
    posts = ForumPost.objects.all().order_by('-pub_datetime')
    context = {
        'posts': posts
    }
    return render(request, 'forum/forum.html', context)


class ForumPostDetailView(generic.DetailView):
    model = ForumPost
    template_name = 'forum/forumpost-details.html'
    queryset = ForumPost.objects.all()
    context_object_name = 'posts'
