# Generated by Django 4.0.3 on 2022-04-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_upload', '0003_alter_dataupload_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
