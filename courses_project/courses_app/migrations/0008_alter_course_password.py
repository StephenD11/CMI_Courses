# Generated by Django 5.1.3 on 2024-11-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0007_alter_course_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='password',
            field=models.CharField(default='default', max_length=100),
        ),
    ]