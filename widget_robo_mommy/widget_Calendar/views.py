from .models import Event, Location
from django.http import HttpResponse


def index(request):
    html_string = 'robo_mommy’s Calendar of Activities<br>'
    for eventItem in Event.objects.all():
        html_string += '''
            <br>
            Date and Time: {}<br>
            Activity: {}<br>
            Estimated Hours: {}<br>
            Course/Section: {}<br>
            Mode: {}<br>
            Venue: {}<br><br>
        '''.format(
            eventItem.target_datetime,
            eventItem.activity,
            eventItem.estimated_hours,
            eventItem.course,
            eventItem.location.mode,
            eventItem.location.venue,
        )
    return HttpResponse(html_string)
