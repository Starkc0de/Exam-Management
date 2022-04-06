# Generated by Django 4.0.3 on 2022-04-06 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('send_notification', '0003_remove_sendnotification_send_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendnotification',
            name='send_notification_by',
        ),
        migrations.AddField(
            model_name='sendnotification',
            name='send_notification_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
