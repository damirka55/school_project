from django import forms

from .models import Course, Lesson, Topic

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['text']
        labels = {'text': ''}

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['text']
        labels = {'text': ''}

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 10})}
