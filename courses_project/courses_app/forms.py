from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {
            'username': 'Придумайте уникальное имя пользователя.',
            'first_name': 'Введите ваше имя.',
            'last_name': 'Введите вашу фамилию.',
            'email': 'Укажите действующий адрес электронной почты.',
            'password1': 'Придумайте надежный пароль (минимум 8 символов).',
            'password2': 'Повторите пароль для подтверждения.',
        }



class CoursePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль курса")


class AssignmentForm(forms.Form):
    assignment_url = forms.URLField(label='Ссылка на тестовое задание', max_length=500)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }