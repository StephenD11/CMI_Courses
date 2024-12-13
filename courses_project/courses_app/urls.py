

from django.urls import path
from . import views

app_name = 'courses_app'  # Указываем пространство имен

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('all_courses/', views.all_courses, name='all_courses'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('course/<int:course_id>/topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('contacts/',views.contacts,name='contacts'),
    path('documents/', views.documents, name='documents'),
    path('profile/', views.profile_view, name='profile'),
    path('course/<int:course_id>/assignment/', views.assignment_view, name='assignment_view'),
    path('update_profile/', views.update_profile_view, name='update_profile'),

]