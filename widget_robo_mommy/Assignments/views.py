from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Assignment, Course
from .forms import AssignmentForm, CourseForm


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
    output = f"Widget's assignments Page<br><br>"
    count = Assignment.objects.all().count()

    for i in range(1, count + 1):
        assignments = Assignment.objects.get(id=i)
        output += f"""Assignment Name: {assignments.name}<br>
                   Description: {assignments.description}<br>
                   Perfect Score: {assignments.perfect_score}<br>
                   Passing Score: {assignments.passing_score}<br>
                   Course/Section: {assignments.course.code} {assignments.course.title}-{assignments.course.section}<br>
                   <br>"""

    return HttpResponse(output)
