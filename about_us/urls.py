from django.urls import path
from . import views

urlpatterns = [
    path('aboutUs', views.AboutUsview, name='about_us_url'),
    # path('home', views.ContactView, name='home'),

]
