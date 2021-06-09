

from django.shortcuts import render
from django.views.generic import ListView
from home.models import Home



# Create your views here.

class Homeview(ListView):
    template_name = "base.html"
    model = Home

