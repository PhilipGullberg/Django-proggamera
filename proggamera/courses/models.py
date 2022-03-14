from pyexpat import model
from django.db import models
from embed_video.fields  import  EmbedVideoField

# Create your models here.

class Videos (models.Model):
    video_title=models.CharField(max_length=50)
    video_descp = models.CharField(max_length=200)
    video = EmbedVideoField()

    def  __str__(self):
	    return  self.video_title

class Quiz (models.Model):
    parent=models.ForeignKey("profilepage.Subchapters", on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class Quizresult(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    students=models.ForeignKey("profilepage.Student", on_delete=models.CASCADE)
    answers=models.CharField(max_length=100)
    result=models.IntegerField()

    def __str__(self):
        return f"{self.students} result for {self.quiz}"

class FillInBlanks(models.Model):
    subchapter=models.ForeignKey("profilepage.Subchapters", on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    description=models.CharField(max_length=200, null=True)
    code_before = models.TextField(max_length=500)
    code_on_input_line_before=models.CharField(max_length=50)
    code_on_input_line_after=models.CharField(max_length=50)
    input_length=models.CharField(max_length=50)
    code_after = models.TextField(max_length=500, blank=True)
    answer=models.CharField(max_length=100, blank=True)
    hint=models.CharField(max_length=500)
    
    
    def __str__(self):
        return f"{self.title}: {self.description}"
