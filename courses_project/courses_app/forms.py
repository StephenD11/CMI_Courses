from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','mid_name')
        help_texts = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
            'mid_name': '',
        }

    # Переопределение полей пароля с пустыми подсказками
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text='',  # Убираем подсказку
    )

    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput,
        help_text='',  # Убираем подсказку
    )


class CoursePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль курса")


class AssignmentForm(forms.Form):
    assignment_url = forms.URLField(label='Ссылка на тестовое задание', max_length=500)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email','mid_name','phone','address','index','city']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mid_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'index': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }