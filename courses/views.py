from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Review
from enrollments.models import Enrollment
from .forms import CourseForm, LessonForm
from django.contrib import messages

# Create your views here.
def course_list(request):
    courses = Course.objects.all()

    if request.user.is_authenticated and request.user.is_instructor:
        filter_type = request.GET.get('filter', 'all')
        if filter_type == 'my':
            courses = courses.filter(instructor=request.user)

    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def create_course(request):
    if not request.user.is_instructor:
        return redirect('home')
    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
        course = form.save(commit=False)
        course.instructor = request.user
        course.save()
        return redirect('course_list')
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Restrict to course owner
    if request.user != course.instructor:
        messages.error(request, "You are not authorized to edit this course.")
        return redirect("course_list")

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect("course_detail", course_id=course.id)
    else:
        form = CourseForm(instance=course)

    return render(request, "courses/edit_course.html", {"form": form, "course": course})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Restrict to course owner
    if request.user != course.instructor:
        messages.error(request, "You are not authorized to delete this course.")
        return redirect("course_list")

    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect("course_list")

    return render(request, "courses/confirm_delete.html", {"course": course})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    reviews = Review.objects.filter(course=course).select_related('student').order_by('-created_at')

    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons, 'is_enrolled': is_enrolled, 'reviews': reviews})

@login_required
def add_lesson(request, course_id):
    # Only instructors can add lessons
    if not request.user.is_instructor:
        return redirect('home')

    course = get_object_or_404(Course, pk=course_id)

    # Ensure that only the instructor who owns the course can add lessons
    if course.instructor != request.user:
        return redirect('home')

    form = LessonForm(request.POST or None)
    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.course = course
        lesson.save()
        return redirect('course_detail', course_id=course.id)

    return render(request, 'courses/add_lesson.html', {
        'form': form,
        'course': course
    })

@login_required
def submit_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.user.is_student and request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            course=course,
            student=request.user,
            rating=rating,
            comment=comment
        )

    return redirect('course_detail', course_id=course.id)