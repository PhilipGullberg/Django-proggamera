from http.client import HTTPResponse
from msilib.schema import Class
from multiprocessing import context
from django.shortcuts import render
from .forms import *
from .models import *
from user.models import *
from django.shortcuts import redirect
from invitations.utils import get_invitation_model
from django.template.loader import render_to_string
# Create your views here.


def teacherdash(request):
    if request.user.is_authenticated:
        if request.user.is_teacher :
            return render(request,'teacherdash.html')
        else:
            user=CustomUser.objects.get(username=request.user.username)
            user.is_teacher=True
            user.save()
            
            return render(request,'teacherdash.html')

def studentdash(request):
    if request.user.is_authenticated:
        if request.user.is_student :
            user=CustomUser.objects.get(username=request.user.username)
            user.is_teacher=True
            return render(request,'teacherdash.html')
        else:
            request.user.is_student = True
            return render(request, 'studentdash.html')
    return render(request, 'studentdash.html')

def t_classroom(request):
    try: 
        curr_user=Teacher.objects.get(user=request.user)
        classes=Classroom.objects.filter(teacher=curr_user)
        
    except Classroom.DoesNotExist:
        classes=[]
    if request.method == 'POST':
        form = add_class_form(request.POST)
        if form.is_valid():
            class_name=form.cleaned_data["class_name"]
            chosen_courses=form.cleaned_data["courses"]
            if request.user.is_teacher:
                user=CustomUser.objects.get(username=request.user.username)
                try:
                    temp_teach=Teacher.objects.get(user=request.user)
                except Teacher.DoesNotExist:
                    add_teacher=Teacher(user=request.user)
                    add_teacher.save()
                    temp_teach=Teacher.objects.get(user=request.user)

                new_classroom=Classroom(name=class_name, teacher=temp_teach)
                new_classroom.save()
                if len(chosen_courses)>1:
                    for i in range(len(chosen_courses)):
                        new_classroom.courses.add(chosen_courses[i])
                else:
                    new_classroom.courses.add(chosen_courses[0])
                new_classroom.save()
                classes=Classroom.objects.filter(name=class_name)
                return redirect( 't_classroom')
            else:
                return render(request,'landing.html')
    else:
        form = add_class_form()

    return render(request, 'teacher_classroom.html',{"form":form,"classes":classes})

def curr_classroom(request, pk):
    classroom = Classroom.objects.get(id=pk)
    courses=Course.objects.filter(classroom__id=pk)
    students=Student.objects.filter(classroom__id=pk)
    """ print("hej")
    curr = request.POST.get('klassnamn', None) 
    curr_classroom=Classroom.objects.filter(name=curr)
    print(curr_classroom)
    #if request.is_ajax and request.method == "POST": """
    context={'classroom':classroom, 'courses':courses,'students':students}
    return render(request,'classroom.html',context)

def add_students(request):
    print("on add_students() ")
    #curr_classroom=Classroom.objects.get(id=classid)
    #print(curr_classroom)
    if request.method == 'POST':
        form = add_student_form(request.POST)
   
        if form.is_valid():
            student=form.cleaned_data["student_name"]
    
    else:
        form=add_student_form()
        student=""
        print(form)
    
    return render(request, 'classroom.html',{"added_students":student,"form":form})

def remove_student(request, student, classroom):
    curr_student=Student.objects.get(id=student)
    curr_classroom=Classroom.objects.get(id=classroom)
    print(curr_student)
    print(curr_classroom)
    curr_classroom.students.remove(curr_student)

    courses=Course.objects.filter(classroom__id=classroom)
    students=Student.objects.filter(classroom__id=classroom)
    context={'classroom':curr_classroom, 'courses':courses,'students':students}
    return render(request,'classroom.html',context)

def add_class(request):
    return render(request,'teacher_classroom.html')
def invite_students(request):
    #change from django-invitations to own model
    #Invitation = get_invitation_model()
    #Invitation.objects.all().delete()
    #todo: Check if user already has been invited for this classroom
    #invite = Invitation.create('philip.gullberg
    #@ntig.se', inviter=request.user)
    #invite.save()
    #invite.send_invitation(request)
    return
def search_students(request):
    
    if request.method=="POST":
        search_text=request.POST.get("search")
        result=Student.objects.filter(user__username__contains=search_text)
    else:
        result=""
    return render(request, 'search_result.html',{'searched_students':result})