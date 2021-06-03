from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactView, name='home'),
    # path('home', views.ContactView, name='home'),

]



