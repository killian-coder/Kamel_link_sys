from django.shortcuts import render
from django.views.generic import ListView
from services.models import Service


# Create your views here.


class ServiceView(ListView):
    template_name = "services.html"
    model = Service
