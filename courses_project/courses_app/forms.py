from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')



class CoursePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль курса")


class AssignmentForm(forms.Form):
    assignment_url = forms.URLField(label='Ссылка на тестовое задание', max_length=500)