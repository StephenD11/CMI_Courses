# Generated by Django 5.1.3 on 2024-11-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0008_alter_course_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='password',
        ),
    ]