# Generated by Django 4.0.3 on 2022-04-04 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_paper', '0004_feedback_student_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='student_data',
            new_name='paper_data',
        ),
    ]
