from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Course, Lesson
from .forms import CourseForm, LessonForm, TopicForm

def index(request):
    """Домашняя страница приложения Project."""
    return render(request, 'project/index.html')
    
def courses(request):
    """Выводит список курсов."""
    courses = Course.objects.order_by('date_added')
    context = {'courses': courses}
    return render(request, 'project/courses.html', context)

def lessons(request, course_id):
    """Выводит список уроков."""
    course = Course.objects.get(id=course_id)
    lessons = course.lesson_set.order_by('-date_added')
    context = {'course': course, 'lessons': lessons}
    return render(request, 'project/course.html', context)

def topic(request, lesson_id):
    """Выводит материал курса."""
    lesson = Lesson.objects.get(id=lesson_id)
    topics = lesson.topic_set.order_by('date_added')
    context = {'lesson': lesson, 'topics': topics}
    return render(request, 'project/lesson.html', context)

def new_course(request):
    """Создает новый курс."""
    if request.method != 'POST':
        #Данные не отправились; создается пустая форма.
        form = CourseForm()
    else:
        #Отправлены данные POST; обработать данные.
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect (reverse('project:courses'))
    
    context = {'form': form}
    return render(request, 'project/new_course.html', context)

def new_lesson(request, course_id):
    """Создает новый урок."""
    course = Course.objects.get(id=course_id)
    
    if request.method != 'POST':
        #Данные не отправились; создается пустая форма.
        form = LessonForm()
    else:
        #Отправлены данные POST; обработать запрос.
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.course = course
            new_lesson.save()
            return HttpResponseRedirect(reverse('project:course',
                args=[course_id]))
                
    context = {'course': course, 'form': form}
    return render(request, 'project/new_lesson.html', context)
    
def new_topic(request, lesson_id):
    """Добавляет материал в урок."""
    lesson = Lesson.objects.get(id=lesson_id)
    
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.lesson = lesson
            new_topic.save()
            return HttpResponseRedirect(reverse('project:lesson',
                args=[lesson_id]))
                
    context = {'lesson': lesson, 'form': form}
    return render(request, 'project/new_topic.html', context)
