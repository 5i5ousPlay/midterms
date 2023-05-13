from .models import Event
from django.http import HttpResponse
from forum.views import convert_utc_to_local
from django.views import generic
from django.urls import reverse


def index(request):
    html_string = '''
    <title>robo_mommy’s Calendar of Activities</title>
    <h2>robo_mommy’s Calendar of Activities</h2><ul>
    '''
    for eventItem in Event.objects.all():
        eventId = str(eventItem.pk)
        href = '<a href="widget_Calendar/Events/'+eventId+'/details">'
        html_string += '''
            <br><li> {}
            Date and Time: {}<br>
            Activity: {}<br>
            Estimated Hours: {}<br>
            Course/Section: {}<br>
            Mode: {}<br>
            Venue: {}<br>
            </li><br>
        '''.format(
            href,
            convert_utc_to_local(eventItem.target_datetime, '%d/%m/%Y|%I:%M %p'),
            eventItem.activity,
            eventItem.estimated_hours,
            eventItem.course.code,
            eventItem.location.mode,
            eventItem.location.venue,
        )
    html_string += '''
        </ul>
        <a href="widget_Calendar/Events/add"><button value="click here">New Activity</button></a><br><br>
        <a href="/Dashboard/">Dashboard</a><br>
        <a href="/announcements/">Announcements</a><br>
        <a href="/forum/">Forum</a><br>
        <a href="/assignments">Assignments</a><br>
        '''
    return HttpResponse(html_string)


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
