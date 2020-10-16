from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Service


# Create your views here.


class ServiceView(TemplateView):
    template_name = "services.html"

    services_list = Service
