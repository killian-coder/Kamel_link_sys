from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('services', TemplateView.as_view(template_name='services.html')),
]
