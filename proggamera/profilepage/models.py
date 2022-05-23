from pyexpat import model
from statistics import mode
from xml.etree.ElementTree import QName
from django.db import models
from courses.models import FillInBlanks, Quiz, VideoWatched, VisitedPage
from user.models import CustomUser
from courses.models import Videos
# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=40)
    def __str__(self):
        return self.course_name
        
class Chapters(models.Model):
    chapter_name=models.CharField(max_length=40)
    chapter_number=models.IntegerField()
    course=models.ForeignKey(Course, on_delete = models.CASCADE)
    def __str__(self):
        return self.chapter_name

class Subchapters(models.Model):
    subchapter_name=models.CharField(max_length=40)
    subchapter_number=models.IntegerField()
    parent_chapter=models.ForeignKey(Chapters, on_delete = models.CASCADE, related_name="sub")
    content=models.TextField(max_length=5000)

    def __str__(self):
        return self.subchapter_name

class Teacher(models.Model):
    user=models.ForeignKey(CustomUser, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username



class Student(models.Model):
    user=models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    courses=models.ManyToManyField(Course, blank=True)
    license_active=models.BooleanField(null=True ,blank=True)
   
    def __str__(self):
        return self.user.username
    

class Classroom(models.Model):
    name=models.CharField(max_length=30)
    students=models.ManyToManyField(Student)
    courses=models.ManyToManyField(Course)
    teacher=models.ForeignKey(Teacher, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    

class Excercise(models.Model):
    classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subchapter=models.ForeignKey(Subchapters, on_delete=models.CASCADE)
    deadline=models.DateField()
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    excercise_type=models.CharField(max_length=64)
    quiz_excercise=models.ForeignKey(Quiz, on_delete=models.SET_NULL, blank=True, null=True)
    fill_excercise=models.ForeignKey(FillInBlanks, on_delete=models.SET_NULL, blank=True, null=True)
    read_excercise=models.ForeignKey(Subchapters, on_delete=models.SET_NULL, blank=True, null=True, related_name="excercise_subchapter")
    video_excercise=models.ForeignKey(Videos, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.excercise_type}: {self.subchapter} for course: {self.course} " 


class ExcerciseResult(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    excercise=models.ForeignKey(Excercise, on_delete=models.CASCADE)
    turned_in=models.BooleanField()
    turned_in_data=models.DateField(auto_now=True)


class StudentExcercises(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    excercises=models.ManyToManyField(Excercise)


    def __str__(self):
        excercise_list=[]
        for excercise in self.excercises.all():
            excercise_list.append(excercise)
        return f'{self.student} har läxorna {excercise_list}'

