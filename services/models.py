from django.db import models


# Create your models here.


class Service(models.Model):
    service_name = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-service_name']
