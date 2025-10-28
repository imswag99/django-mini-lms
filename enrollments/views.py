from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Enrollment
from courses.models import Course

# Create your views here.

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk = course_id)
    Enrollment.objects.get_or_create(student = request.user, course = course)
    return redirect('course_detail', course_id = course_id)


@login_required
def unenroll_course(request, course_id):
    course = get_object_or_404(Course, pk = course_id)
    Enrollment.objects.filter(student = request.user, course = course).delete()
    return redirect('course_list')