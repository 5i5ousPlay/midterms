import string
from .models import WidgetUser, Department
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse


def Dashboard_list_view(request):
    html_string_1 = '<html lang="en"><head><meta charset="UTF-8">' \
                    '<h1>Welcome to Widget</h1>' \
                    '<h2>WIDGET USERS</h2></head><ul>'
    html_string_2 = ''
    for wu in WidgetUser.objects.all():
        number = str(wu.pk)
        href = '<a href="/Widgetusers/' + number + '/details">'
        html_string_2 += '<li>' + href + '{}, {} {}: {}, {}' .format(wu.last_name, 
                                                         wu.first_name,
                                                         wu.middle_name,
                                                         wu.department.dept_name,
                                                         wu.department.home_unit)
    html_string_2 += '</ul></li>'
    html_string_3 = '<a href="/Widgetusers/add"><button value="click here" > Add Widget User</button></a><br><br>'
    html_string_3 += '<a href="/Announcements/">Announcement Board</a><br>'
    html_string_3 += '<a href="/Forum/">Forum</a><br>'
    html_string_3 += '<a href="/Assignments">Assignment</a><br>'
    html_string_3 += '<a href="/Calendar/">Calendar</a><br>'
    html_string_final = html_string_1 + html_string_2 + html_string_3 + '</html>'

    
    return HttpResponse(html_string_final)



class WidgetUserDetailView(generic.DetailView):
    model = WidgetUser
    template_name = 'widgetuser-details.html'
    queryset = WidgetUser.objects.all()
    context_object_name = 'widgetuser-detail'

class WidgetUserAddView(generic.CreateView):
    model = WidgetUser
    fields = '__all__'
    template_name = 'widgetuser-add.html'

    def get_success_url(self):
        return reverse('Dashboard:widgetuser-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)


class WidgetUserUpdateView(generic.UpdateView):
    model = WidgetUser
    template_name = 'widgetuser-edit.html'
    fields = '__all__'
    success_url = "Dashboard/"

    def get_success_url(self):
        return reverse('Dashboard:widgetuser-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)
    