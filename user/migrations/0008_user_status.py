# Generated by Django 4.0.3 on 2022-04-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
