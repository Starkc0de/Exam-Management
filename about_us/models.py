from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)