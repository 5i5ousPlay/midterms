from .models import Department
from django.views import generic


class DashboardView(generic.ListView):
    model = Department
    template_name = 'Dashboard/Dashboard.html'
