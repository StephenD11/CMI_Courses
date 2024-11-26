from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]