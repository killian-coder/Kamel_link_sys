from django.shortcuts import render
from django.views.generic import ListView
from about_us.models import About



# Create your views here.

class AboutUsview(ListView):
    template_name = "about.html"
    model = About

