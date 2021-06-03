

from django.shortcuts import render
from django.views.generic import ListView
from .models import Home



# Create your views here.


class HomeView(ListView):
    template_name = "base.html"
    model = Home

