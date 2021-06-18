from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-title']