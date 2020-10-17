from django.shortcuts import render, redirect
from .models import ContactDetails, ContactUs


# Create your views here.

def contact_us(request):
    c = ContactDetails.objects.all()
    return redirect(c)

