from django.contrib import admin
from .models import Course, Lesson, Review

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Review)