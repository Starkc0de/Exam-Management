import email
from unicodedata import name
from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=225, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)