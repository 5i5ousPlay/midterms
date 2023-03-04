from django.shortcuts import render
from django.http import HttpResponse
from .models import Assignment, Course


def index(request):
    output = f"Widget's Assignments Page\n"
    count = Assignment.objects.all().count()

    for i in range(1, count + 1):
        assignments = Assignment.objects.get(id=i)
        courses = Course.objects.get(id=i)
        output += (f"Assignment Name: {assignments.mame}\n"
                   f"Description: {assignments.description}\n"
                   f"Perfect Score: {assignments.perfect_score}\n"
                   f"Passing Score: {assignments.passing_score}\n"
                   f"Course/Section: {courses.code} {courses.title}-{courses.section}\n\n")

    return HttpResponse(output)
