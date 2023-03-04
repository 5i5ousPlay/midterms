from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Welcome to Cheska's Music Library!")
