from django.contrib import admin
from django.urls import path, include
from myApp import views

app_name = 'myApp'

## student_pk and course_pk defined both in the models.py file and the templates as well.

urlpatterns = [
    path('', views.courseListView.as_view(), name='course-list'),
    path('createCourse', views.courseCreateView.as_view(), name='course-create'),
    path('course-<int:course_pk>/', views.courseDetailView.as_view(), name='course-detail'),
    path('course-<int:course_pk>/update', views.courseUpdateView.as_view(), name='course-update'),
    path('course-<int:course_pk>/delete', views.courseDeleteView.as_view(), name='course-delete'),
    path('student-<int:student_pk>/', views.studentDetailView.as_view(), name='student-detail'),
    path('student-<int:student_pk>/update', views.studentUpdateView.as_view(), name='student-update'),
    path('student-<int:student_pk>/delete', views.studentDeleteView.as_view(), name='student-delete'),
    path('createStudent', views.studentCreateView.as_view(), name='student-create'),
]