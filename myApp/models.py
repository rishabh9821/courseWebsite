from django.db import models
from django.urls import reverse


options = [('Math', 'Math'), ('Computer Science','Computer Science'),('History','History'), ('Undecided', 'Undecided'), ('English','English'), ('Science', 'Science') ]
subjects = [('Math', 'Math'), ('Computer Science','Computer Science'),('History','History'), ('English','English'), ('Science', 'Science') ]

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length = 64)
    courseSubject = models.CharField(choices = subjects, max_length = 64)
    courseProfessor = models.CharField(max_length = 64)
    #courseStudents = models.ManyToManyField('Student', related_name='courses')

    def __str__(self):
        return str(self.courseName)

    def get_absolute_url(self):
        return reverse('myApp:course-detail', kwargs={'course_pk': self.pk})


class Student(models.Model):
    studentName = models.CharField(max_length = 64)
    studentMajor = models.CharField(choices = options, max_length = 64)
    studentMinor = models.CharField(choices = options, blank = True, max_length = 64)

    studentCourses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return str(self.studentName)
    
    def get_absolute_url(self):
        return reverse('myApp:student-detail', kwargs={'student_pk': self.pk})