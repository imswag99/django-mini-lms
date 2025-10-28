from django.shortcuts import render
from django.shortcuts import render
from courses.models import Course

def popular_courses(request):
    courses = Course.objects.all()  # get all courses
    return render(request, 'index.html', {'courses': courses})

def about(request):
    return render(request, 'about.html')