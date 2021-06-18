from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview, name='home_url'),
    # path('home', views.ContactView, name='home'),

]



