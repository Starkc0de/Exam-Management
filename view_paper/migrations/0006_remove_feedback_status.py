# Generated by Django 4.0.3 on 2022-04-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_paper', '0005_rename_student_data_feedback_paper_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='status',
        ),
    ]
