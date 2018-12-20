from django.contrib import admin

from project.models import Course, Lesson, Topic

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Topic)
