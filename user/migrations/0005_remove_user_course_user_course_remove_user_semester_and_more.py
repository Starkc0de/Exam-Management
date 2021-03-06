# Generated by Django 4.0.3 on 2022-04-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_upload', '0004_alter_dataupload_status'),
        ('user', '0004_user_course_user_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='course',
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(blank=True, to='data_upload.course'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='semester',
        ),
        migrations.AddField(
            model_name='user',
            name='semester',
            field=models.ManyToManyField(blank=True, to='data_upload.semester'),
        ),
    ]
