# Generated by Django 4.0.3 on 2022-04-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_notification', '0005_alter_sendnotification_send_notification_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendnotification',
            name='notification_status',
            field=models.BooleanField(default=True),
        ),
    ]
