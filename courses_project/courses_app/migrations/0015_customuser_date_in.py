# Generated by Django 5.1.3 on 2024-12-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0014_alter_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_in',
            field=models.DateField(blank=True, null=True, verbose_name='Дата зачисления'),
        ),
    ]
