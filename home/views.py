from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("hallo,  World this is the home page")
    return render(request, 'index.html')
