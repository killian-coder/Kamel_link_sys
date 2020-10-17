from django.urls import path
from django.views.generic import TemplateView
from .views import ServiceView

urlpatterns = [
    path('services/', ServiceView.as_view()),
]
