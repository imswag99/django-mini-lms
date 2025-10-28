from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/create/', views.create_course, name='create_course'),
    path("course/<int:course_id>/edit/", views.edit_course, name="edit_course"),
    path("course/<int:course_id>/delete/", views.delete_course, name="delete_course"),
    path('course/<int:course_id>/add-lesson/', views.add_lesson, name='add_lesson'),
    path('course/<int:course_id>/review/', views.submit_review, name='submit_review'),

]
