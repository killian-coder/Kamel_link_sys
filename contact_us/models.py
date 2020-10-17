from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=200, help_text="Name of Sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email

class ContactDetails(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural = "Details"

    def __str__(self):
        return self.address + "-" + self.phone_number
