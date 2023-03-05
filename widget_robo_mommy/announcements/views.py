from django.shortcuts import render
from django.http import HttpResponse
from .models import Announcement, Reaction
import pytz
from django.utils import timezone


def convert_to_localtime(utctime):
    format = '%d/%m/%Y %H:%M'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(format)


def index(request):
    html_string_1 = '<html lang="en"><head><meta charset="UTF-8"></head>\
                    <b><h1>Widget\'s Announcement Board</h1></b>\
                    <h2>Announcements:</h2><br/>'
    
    html_string_2 = ""
    for announced in Announcement.objects.all():
        html_string_2 += "{} by {} {} published {}<br />:\
                        {}".format(announced.title, announced.author.first_name,
                        announced.author.last_name,
                        convert_to_localtime(announced.pub_datetime), announced.body)
        for reacts in announced.reaction.all():
            html_string_2 += "{}: {}".format(reacts.name, reacts.tally)
    
    html_string_final = html_string_1 + html_string_2 + "</html>"
    
    return HttpResponse(html_string_final)

# Create your views here.
