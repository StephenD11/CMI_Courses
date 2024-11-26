# Generated by Django 5.1.3 on 2024-11-26 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('order', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='courses_app.course')),
            ],
        ),
    ]
