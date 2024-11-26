from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug
from django.contrib.auth import get_user_model




# Модель пользователя
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),  # Администратор
        ('student', 'Student'),  # Обучающийся
        ('user', 'User'),  # Обычный пользователь
    ]

    # Поле для логина пользователя, должно быть уникальным
    # Здесь используется валидация, чтобы имя пользователя соответствовало слагу (т.е. только буквы, цифры и дефисы)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Введите имя пользователя [150 символов или меньше]',
        error_messages={'unique':"Такое имя уже существует, выбирете другое"},
        verbose_name='Логин'
    )
    # Поле для email пользователя, оно также уникально
    email = models.EmailField(
        unique=True,  # Email должен быть уникальным
        verbose_name='Почта'  # Название поля в админке
    )

    # Поле для роли пользователя, которое может быть: admin, student или user
    role = models.CharField(
        max_length=10,  # Максимальная длина для значения роли
        choices=ROLE_CHOICES,  # Ограничиваем выбор только этими тремя значениями
        default='user',  # По умолчанию роль будет 'user'
        verbose_name='Роль'  # Название поля в админке
    )

    def __str__(self):
        return self.username  # При отображении пользователя выводится его имя (логин)

# Модель курса
class Course(models.Model):
    title = models.CharField(max_length=255)  # Название курса
    description = models.TextField()  # Описание курса
    created_at = models.DateTimeField(auto_now_add=True) # устанавливает текущее время при создании

    # Связь с пользователями (студентами). Один курс может быть связан с несколькими пользователями
    students = models.ManyToManyField(get_user_model(), related_name='courses')  #Связь многие ко многим

    def __str__(self):
        return self.title


# Модель темы курса
class CourseTopic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)  # Связь с курсом
    title = models.CharField(max_length=255)  # Название темы
    content = models.TextField()  # Контент темы
    order = models.IntegerField()  # Порядок отображения темы (по номеру)

    def __str__(self):
        return f'{self.course.title} - {self.title}'


