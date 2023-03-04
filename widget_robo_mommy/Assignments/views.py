from django.shortcuts import render
from django.http import HttpResponse
from .models import Assignment, Course
import os


def index(request):
    output = f"Widget's Assignments Page<br><br>"
    count = Assignment.objects.all().count()

    for i in range(1, count + 1):
        assignments = Assignment.objects.get(id=i)
        courses = Course.objects.get(id=i)
        output += f"""Assignment Name: {assignments.name}<br>
                   Description: {assignments.description}<br>
                   Perfect Score: {assignments.perfect_score}<br>
                   Passing Score: {assignments.passing_score}<br>
                   Course/Section: {assignments.course.code} {assignments.course.title}-{cassignments.course.section}<br>
                   <br>"""

    return HttpResponse(output)
