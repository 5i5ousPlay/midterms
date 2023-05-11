from .models import WidgetUser, Department
from django.http import HttpResponse
from django.shortcuts import render


def Dashboard_list_view(request):
    html_string_1 = '<html lang="en"><head><meta charset="UTF-8">' \
                    '<h1>Welcome to Widget</h1>' \
                    '<h2>WIDGET USERS</h2></head><ul>'
    html_string_2 = ''
    for wu in WidgetUser.objects.all():
        html_string_2 += '<li>{}, {} {}: {}, {}' .format(wu.last_name, 
                                                         wu.first_name,
                                                         wu.middle_name,
                                                         wu.department.dept_name,
                                                         wu.department.home_unit)
    html_string_2 += '</ul></li>'
    html_string_final = html_string_1 + html_string_2 + '</html>'

    return HttpResponse(html_string_final)
