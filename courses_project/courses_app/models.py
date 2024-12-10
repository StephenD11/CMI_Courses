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

    LEARN_CHOICES = [
        ('python1', 'Python:Начинающий'),  # Администратор
        ('python2', 'Python:Продвинутый'),  # Администратор
        ('java1', 'Java:Начинающий'),  # Обучающийся
        ('java2', 'Java:Продвинутый'),  # Обучающийся
        ('sql', 'SQL'),  # Обычный пользователь
        ('js', 'JS'),  # Обычный пользователь
        ('html', 'HTML/CSS'),  # Обычный пользователь
    ]

    # Поле для логина пользователя, должно быть уникальным
    # Здесь используется валидация, чтобы имя пользователя соответствовало слагу (т.е. только буквы, цифры и дефисы)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Введите имя пользователя',
        error_messages={'unique': "Такое имя уже существует, выбирете другое"},
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

    link_work = models.CharField(
        max_length=500,
        default='',
        verbose_name='Ссылка на работу'
    )

    mid_name = models.CharField(default='Неизвестно', max_length=100,verbose_name='Отчество', blank=True)
    phone = models.CharField(default='Неизвестно', max_length=100,verbose_name='Телефон', blank=True)
    learn = models.CharField(
        default='Нет курса',

        max_length=100,
        verbose_name='Направление',
        blank=True,
        choices=LEARN_CHOICES,  # Ограничиваем выбор только этими тремя значениями
    )


    date_in = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата зачисления"
    )

    date_out = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата окончания"
    )

    date_pay = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата оплаты"
    )

    city = models.CharField(default='Неизвестно', max_length=50,verbose_name='Город', blank=True)
    address = models.CharField(default='Неизвестно', max_length=50,verbose_name='Адрес', blank=True)
    index = models.CharField(default='Неизвестно', max_length=50,verbose_name='Индекс', blank=True)


    def __str__(self):
        return self.username  # При отображении пользователя выводится его имя (логин)


# Модель курса
class Course(models.Model):
    title = models.CharField(max_length=255,verbose_name='Курс')  # Название курса
    description = models.TextField(verbose_name='Описание')  # Описание курса
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')  # устанавливает текущее время при создании

    # Связь с пользователями (студентами). Один курс может быть связан с несколькими пользователями
    students = models.ManyToManyField(get_user_model(), related_name='courses',verbose_name='Студент')  # Связь многие ко многим
    password = models.CharField(max_length=30, null=False, blank=False, default='default',verbose_name='Пароль')

    class Meta:
        verbose_name = 'Курс'  # Единственное число
        verbose_name_plural = 'Курсы'  # Множественное число

    def __str__(self):
        return self.title


# Модель темы курса
class Topic(models.Model):
    course = models.ForeignKey(
        Course,  # Связываем тему с конкретным курсом через внешний ключ
        on_delete=models.CASCADE,  # Указываем, что удаление курса приведёт к удалению всех его тем
        related_name='topics',
        verbose_name='Курс'
    )

    title = models.CharField(max_length=200,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    order = models.PositiveIntegerField(default=0,verbose_name='Номер темы')  # Поле для сортировки тем в курсе
    is_completed = models.BooleanField(default=False,verbose_name='Завершен')  # Флаг для отслеживания завершения темы

    class Meta:
        verbose_name = 'Тема'  # Единственное число
        verbose_name_plural = 'Темы'  # Множественное число

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='question',verbose_name='Темы')
    question_text = models.CharField(max_length=500,verbose_name='Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'  # Единственное число
        verbose_name_plural = 'Вопросы'  # Множественное число

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Ответ'  # Единственное число
        verbose_name_plural = 'Ответы'  # Множественное число


    def __str__(self):
        return self.answer_text


class AssignmentSubmission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='Слушатель')  # Привязка к пользователю
    assignment_url = models.URLField(max_length=800,verbose_name='Ссылка')  # Ссылка на тест
    submitted_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата')  # Дата отправки

    class Meta:
        verbose_name = 'Контрольная работа'  # Единственное число
        verbose_name_plural = 'Контрольные работы'  # Множественное число

    def __str__(self):
        return f"Тест {self.assignment_url} от {self.user}"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.created_at}"