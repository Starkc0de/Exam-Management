from django.db import models
from user.models import User
from data_upload.models import DataUpload

# Create your models here.

class FeedBack(models.Model):
    feedback_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    paper_data = models.ForeignKey(DataUpload, on_delete=models.CASCADE,null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    return_feedback = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'FeedBack'
        verbose_name_plural = 'FeedBack'

    def __str__(self) -> str:
        return self.comment
