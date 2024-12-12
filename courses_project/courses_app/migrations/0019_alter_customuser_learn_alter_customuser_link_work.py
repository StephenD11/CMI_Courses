# Generated by Django 5.1.3 on 2024-12-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0018_customuser_learn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='learn',
            field=models.CharField(blank=True, choices=[('python1', 'Python:Начинающий'), ('python2', 'Python:Продвинутый'), ('java1', 'Java:Начинающий'), ('java2', 'Java:Продвинутый'), ('sql', 'SQL'), ('js', 'JS'), ('html', 'HTML/CSS')], default='Нет курса', max_length=100, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='link_work',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Ссылка на работу'),
        ),
    ]
