from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Assignment
from .forms import AssignmentForm


class AssignmentDetailsView(DetailView):
    model = Assignment
    template_name = 'assignments/assignment-details.html'


class AddAssignmentView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignments/assignment-add.html'


class EditAssignmentView(UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignments/assignment-edit.html'


def index(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignments/assignments.html', context)
