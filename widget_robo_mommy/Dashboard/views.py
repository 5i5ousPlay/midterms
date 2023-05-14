from django.shortcuts import render
from .models import WidgetUser
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse


def Dashboard_list_view(request):
    users = WidgetUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/dashboard.html', context)




class WidgetUserDetailView(generic.DetailView):
    model = WidgetUser
    template_name = 'dashboard/widgetuser-details.html'
    queryset = WidgetUser.objects.all()
    context_object_name = 'widgetuser-detail'


class WidgetUserAddView(generic.CreateView):
    model = WidgetUser
    fields = '__all__'
    template_name = 'dashboard/widgetuser-add.html'

    def get_success_url(self):
        return reverse('Dashboard:widgetuser-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)


class WidgetUserUpdateView(generic.UpdateView):
    model = WidgetUser
    template_name = 'dashboard/widgetuser-edit.html'
    fields = '__all__'
    success_url = "dashboard/"

    def get_success_url(self):
        return reverse('Dashboard:widgetuser-detail', kwargs={'pk': self.object.id},
                       current_app=self.request.resolver_match.namespace)
