# Generated by Django 4.0.3 on 2022-03-28 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name': 'Semester', 'verbose_name_plural': 'Semester'},
        ),
    ]
