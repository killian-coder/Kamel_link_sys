from django.shortcuts import render
from django.views.generic import ListView
from .models import ContactUs



# Create your views here.


class ContactView(ListView):
    template_name = "contact.html"
    model = ContactUs