from django.shortcuts import render
from .models import Event
from django.http import HttpResponse
from forum.views import convert_utc_to_local
from django.views import generic
from django.urls import reverse


def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'widget_Calendar/calendar.html', context)


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'widget_Calendar/event-details.html'
    queryset = Event.objects.all()
    context_object_name = 'event-detail'


class EventAddView(generic.CreateView):
    model = Event
    fields = '__all__'
    template_name = 'widget_Calendar/event-add.html'

    def get_success_url(self):
        return reverse('widget_Calendar:event-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)


class EventUpdateView(generic.UpdateView):
    model = Event
    template_name = 'widget_Calendar/event-edit.html'
    fields = '__all__'
    success_url = "widget_Calendar/"

    def get_success_url(self):
        return reverse('widget_Calendar:event-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)
