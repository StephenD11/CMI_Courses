# Generated by Django 5.1.3 on 2024-11-28 13:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0010_course_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_url', models.URLField(max_length=500)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
