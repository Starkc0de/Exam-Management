from django.db import models
from user.models import User


# Create your models here.

class SendNotification(models.Model):
    send_notification_by = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    notification_status=models.BooleanField(default=True)

    class Meta:
        verbose_name = 'SendNotification'
        verbose_name_plural = 'SendNotification'

    def __str__(self) -> str:
        return self.title
