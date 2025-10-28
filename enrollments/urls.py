from django.urls import path
from . import views

urlpatterns = [
    # Enroll a student in a course
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),

    # Unenroll from a course
    path('unenroll/<int:course_id>/', views.unenroll_course, name='unenroll_course'),
]