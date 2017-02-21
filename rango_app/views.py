from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(
        "Rango bango!!!<br><a href=\"/rango/about/\">Go to ABOUT page</a>")

def about(request):
    return HttpResponse(
        "This is ABOUT page. <a href=\"/rango/\">To the main Rango page</a>")

