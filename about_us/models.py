from django.db import models

# Create your models here.

class About(models.Model):
    about_title = models.CharField(max_length=30)
    wording = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-about_title']

