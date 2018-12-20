"""Определяет схемы URL для Project."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'project'
urlpatterns = [
    #Домашняя страница.
    path('', views.index, name='index'),
    
    #Вывод все курсы.
    path('courses/', views.courses, name='courses'),
    
    #Вывод уроков.
    path('courses/<int:course_id>/', views.lessons, name='course'),
    
    #Вывод материaла.
    path('<int:lesson_id>/', views.topic, name='lesson'),
    
    #Страница для добавления нового курса.
    path('new_course/', views.new_course, name='new_course'),
    
    #Страница для добавления нового урока.
    path('new_lesson/<int:course_id>/', views.new_lesson, name='new_lesson'),
    
    #Страница для добавления новой темы.
    path('new_topic/<int:lesson_id>/', views.new_topic, name='new_topic'),
    
    #Страница для редактирования материалов.
    path('edit_topic/<int:lesson_id>/', views.edit_topic, name='edit_topic'),
    ]
