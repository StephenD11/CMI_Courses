from tkinter.font import names

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Topic, AssignmentSubmission
from django.shortcuts import redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomUserCreationForm,CoursePasswordForm, AssignmentForm
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
def index(request):
    courses = Course.objects.all()  # Получаем все курсы из базы данных
    return render(request, 'courses_app/index.html', {'courses': courses})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/')  # Перенаправление после логина
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'courses_app/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Перенаправляем на страницу успешной регистрации
            return redirect('courses_app:registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'courses_app/register.html', {'form': form})

def registration_success_view(request):
    return render(request, 'courses_app/registration_success.html')


def logout_view(request):
    logout(request)
    return redirect('courses_app:login')  # Перенаправляем на страницу логина после выхода


@login_required
def course_detail(request, course_id):
    # Получаем курс по ID
    course = get_object_or_404(Course, id=course_id)

    # Проверяем, был ли введен правильный пароль ранее
    password_valid = request.session.get(f'password_valid_{course.id}', False)

    # Если пароль еще не был введен или не верный, показываем форму
    form = CoursePasswordForm()  # Всегда создаем форму

    if not password_valid:
        if request.method == 'POST':
            form = CoursePasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                if password == course.password:  # Проверка пароля
                    request.session[f'password_valid_{course.id}'] = True  # Сохраняем успешный ввод пароля в сессии
                    password_valid = True  # Обновляем переменную, чтобы темы показывались
                else:
                    messages.error(request, 'Неверный пароль')  # Сообщение о неправильном пароле

    return render(request, 'courses_app/course_detail.html',
                  {'course': course, 'form': form, 'password_valid': password_valid})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses_app/all_courses.html', {'courses': courses})


def topic_detail(request, course_id, topic_id):
    course = get_object_or_404(Course, id=course_id)
    topic = get_object_or_404(Topic, id=topic_id)

    # Получаем соседние темы
    previous_topic = Topic.objects.filter(course=course, id__lt=topic.id).last()
    next_topic = Topic.objects.filter(course=course, id__gt=topic.id).first()

    return render(request, 'courses_app/topic_detail.html', {
        'course': course,
        'topic': topic,
        'previous_topic': previous_topic,
        'next_topic': next_topic,
    })

def documents(request):
    return render(request, 'courses_app/documents.html')

def contacts(request):
    return render(request, 'courses_app/contacts.html')


@login_required
def profile_view(request):
    # Получаем текущего пользователя
    user = request.user
    # Получаем курсы, к которым у него есть доступ
    courses = user.courses.all()
    return render(request, 'courses_app/profile.html', {'user': user, 'courses': courses})


# views.py
@login_required
def topic_detail(request, course_id, topic_id):
    course = Course.objects.get(id=course_id)
    topic = course.topics.get(id=topic_id)
    user = request.user

    # Логика для обновления завершенности темы
    if request.method == 'POST':
        # Проверка, если нажата кнопка "Завершить тему"
        if 'complete' in request.POST:
            topic.is_completed = True
            topic.save()
        # Проверка, если нажата кнопка "Отменить завершение"
        elif 'undo' in request.POST:
            topic.is_completed = False
            topic.save()

    # Получаем все темы курса
    topics = course.topics.all()

    # Ищем завершенные темы для прогресса
    user_topics = [topic for topic in topics if topic.is_completed]

    # Навигация по темам (предыдущая и следующая тема)
    previous_topic = course.topics.filter(id__lt=topic.id).last()
    next_topic = course.topics.filter(id__gt=topic.id).first()

    return render(request, 'courses_app/topic_detail.html', {
        'course': course,
        'topic': topic,
        'user_topics': user_topics,
        'previous_topic': previous_topic,
        'next_topic': next_topic
    })


@login_required
def assignment_view(request, course_id):
    course = Course.objects.get(id=course_id)

    # Просто отображаем страницу задания без проверки завершенности курса
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            # Сохраняем ссылку на тестовое задание
            AssignmentSubmission.objects.create(
                user=request.user,
                assignment_url=form.cleaned_data['assignment_url']
            )
            return redirect('courses_app:profile')  # Перенаправляем на профиль после успешной отправки
    else:
        form = AssignmentForm()

    return render(request, 'courses_app/work.html', {
        'course': course,
        'form': form
    })

