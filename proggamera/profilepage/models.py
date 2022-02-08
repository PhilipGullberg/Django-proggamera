from django.db import models
from user.models import CustomUser

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=40)
    def __str__(self):
        return self.course_name
        
class Chapters(models.Model):
    chapter_name=models.CharField(max_length=40)
    course=models.ForeignKey(Course, on_delete = models.CASCADE)
    def __str__(self):
        return self.chapter_name

class Student(models.Model):
    user=models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    courses=models.ManyToManyField(Course, blank=True)
    license_active=models.BooleanField()
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user=models.ForeignKey(CustomUser, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Classroom(models.Model):
    name=models.CharField(max_length=30)
    students=models.ManyToManyField(Student)
    courses=models.ManyToManyField(Course)
    teacher=models.ForeignKey(Teacher, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
