# Generated by Django 5.1.3 on 2024-12-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0017_alter_customuser_mid_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='learn',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('java', 'Java'), ('sql', 'SQL'), ('js', 'JS')], default='Нет курса', max_length=100, verbose_name='Направление'),
        ),
    ]