from re import template
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myApp.models import Student, Course
# Create your views here.




class courseListView(ListView):
    model = Course
    template_name = 'myApp/courseList.html'
    context_object_name = 'course_list'

class courseDetailView(DetailView):
    context_object_name = 'course_detail'
    model = Course
    template_name = 'myApp/courseDetail.html'
    pk_url_kwarg = 'course_pk'

class studentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = Student
    template_name = 'myApp/studentDetail.html'
    pk_url_kwarg = 'student_pk'

    def get_context_data(self, **kwargs):
        kwargs['courses'] = Course.objects.filter(students = self.object)
        # print(Course.objects.filter(students = self.object).all())
        return super().get_context_data(**kwargs)

class studentCreateView(CreateView):
    model = Student
    fields = ('studentName', 'studentMajor', 'studentMinor', 'studentCourses')
    template_name = 'myApp/student_form.html'
     
    ## Need to provide a get_absolute_url function in the model to redirect

class studentUpdateView(UpdateView):
    model = Student
    fields = ('studentName', 'studentMajor', 'studentMinor', 'studentCourses')
    template_name = 'myApp/student_form.html'
    pk_url_kwarg = 'student_pk'
    

class courseCreateView(CreateView):
    model = Course
    fields = ('courseName', 'courseSubject', 'courseProfessor')
    template_name = 'myApp/course_form.html'

class courseUpdateView(UpdateView):
    model = Course
    fields = ('courseName', 'courseSubject', 'courseProfessor')
    template_name = 'myApp/course_form.html'
    pk_url_kwarg = 'course_pk'

class studentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('myApp:course-list')
    pk_url_kwarg = 'student_pk'

class courseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    success_url = reverse_lazy('myApp:course-list')
    pk_url_kwarg = 'course_pk'


