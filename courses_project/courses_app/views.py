from tkinter.font import names

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from django.shortcuts import redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomUserCreationForm


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
            form.save()
            return redirect('login')  # Перенаправление на страницу логина
    else:
        form = CustomUserCreationForm()
    return render(request, 'courses_app/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу логина после выхода


@login_required
def course_detail(request, course_id):
    # Получаем курс по ID
    course = get_object_or_404(Course, id=course_id)

    # Передаем курс в шаблон, независимо от роли пользователя
    return render(request, 'courses_app/course_detail.html', {'course': course})
