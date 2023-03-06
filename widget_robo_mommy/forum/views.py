from django.shortcuts import render
from django.http import HttpResponse
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
    html_string_1 = '<html lang="en"><head><meta charset="UTF-8"><title>Forum Post List</title>' \
                    '<h1>Forum Post List</h1></head><ul>'
    html_string_2 = ''
    for fp in ForumPost.objects.all():
        html_string_2 += '<li><b style="font-size: 30px">{}</b>' \
                         ' by <b style="font-size: large">{} {}</b>' \
                         ' posted <b>{}</b><p>{}</p><ul>'.format(fp.title,
                                                                 fp.author.first_name,
                                                                 fp.author.last_name,
                                                                 convert_utc_to_local(fp.pub_datetime,
                                                                                      '%d/%m/%Y %I:%M %p'),
                                                                 fp.body)
        for replies in fp.reply.all():
            html_string_2 += '<li> Reply by <b>{} {}</b> ' \
                             'posted <b>{}</b><p>{}</p></li>'.format(replies.author.first_name,
                                                                     replies.author.last_name,
                                                                     convert_utc_to_local(replies.pub_datetime,
                                                                                          '%d/%m/%Y %I:%M %p'),
                                                                     replies.body)
        html_string_2 += '</ul></li>'
    html_string_final = html_string_1 + html_string_2 + '</ul></html>'

    return HttpResponse(html_string_final)
