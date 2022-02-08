from django.shortcuts import render

# Create your views here.
def course(request,courseid):
    course=courseid
    return render(request,"course.html",{"course":course})