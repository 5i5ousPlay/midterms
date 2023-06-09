from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Announcement, Reaction
import pytz
from django.utils import timezone


def convert_to_localtime(utctime):
    format = '%m/%d/%Y %I:%M %p'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(format)

def index(request):
    announcement = Announcement.objects.all().order_by('-pub_datetime')
    context = {
        'announcement': announcement
    }
    
    return render(request, 'announcements/announcements.html', context)

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement-details.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announce'

class AnnouncementAddView(CreateView):
    model = Announcement
    fields =  ['title', 'body', 'author']
    template_name = 'announcements/announcement-add.html'
    
    def get_success_url(self):
        return reverse('announcements:announcementdetailview', kwargs={'pk': self.object.id},
            current_app=self.request.resolver_match.namespace)

class AnnouncementEditView(UpdateView):
    model = Announcement
    template_name = 'announcements/announcement-edit.html'
    fields = ['title', 'body', 'author']

    def get_success_url(self):
        return reverse('announcements:announcementdetailview', kwargs={'pk': self.object.id},
            current_app=self.request.resolver_match.namespace)

# Create your views here.
