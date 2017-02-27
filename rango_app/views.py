from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Pamparam kio mio, Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango_app/index.html', context=context_dict)
    # return HttpResponse(
    #     "Rango bango!!!<br><a href=\"/rango/about/\">Go to ABOUT page</a>")

def about(request):
    return render(request, 'rango_app/about.html')
    # return HttpResponse(
    #     "This is ABOUT page. <a href=\"/rango/\">To the main Rango page</a>")

