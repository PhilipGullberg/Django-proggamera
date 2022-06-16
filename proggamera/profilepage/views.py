from email import message
from http.client import HTTPResponse
from msilib.schema import Class
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from courses.models import Quiz, VisitedPage
from courses.models import FillInBlanks, Videos
from .forms import *
from .models import Course, Chapters, StudentExcercises, Subchapters, Student, Teacher, Classroom, Excercise, ExcerciseResult
from user.models import *
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.


def teacherdash(request):
    curr_teacher = Teacher.objects.get(user=request.user)
    teachers_classrooms = Classroom.objects.filter(teacher=curr_teacher)
    teachers_courses = Course.objects.filter(classroom__teacher=curr_teacher)
    courses = []
    for course in teachers_courses:
        if course not in courses:
            courses.append(course)
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return render(request, 'teacherdash.html', {'classrooms': teachers_classrooms, 'courses': courses})


def studentdash(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            user = CustomUser.objects.get(username=request.user.username)
            user.is_student = True
            user.save()
            return render(request, 'studentdash.html')
        else:
            request.user.is_student = True
            return render(request, 'studentdash.html')
    return render(request, 'studentdash.html')


def t_classroom(request):
    try:
        curr_user = Teacher.objects.get(user=request.user)
        classes = Classroom.objects.filter(teacher=curr_user)

    except Classroom.DoesNotExist:
        classes = []
    if request.method == 'POST':
        form = add_class_form(request.POST)
        if form.is_valid():
            class_name = form.cleaned_data["class_name"]
            chosen_courses = form.cleaned_data["courses"]
            if request.user.is_teacher:
                user = CustomUser.objects.get(username=request.user.username)
                try:
                    temp_teach = Teacher.objects.get(user=request.user)
                except Teacher.DoesNotExist:
                    add_teacher = Teacher(user=request.user)
                    add_teacher.save()
                    temp_teach = Teacher.objects.get(user=request.user)

                new_classroom = Classroom(name=class_name, teacher=temp_teach)
                new_classroom.save()
                if len(chosen_courses) > 1:
                    for i in range(len(chosen_courses)):
                        new_classroom.courses.add(chosen_courses[i])
                else:
                    new_classroom.courses.add(chosen_courses[0])
                new_classroom.save()
                classes = Classroom.objects.filter(name=class_name)
                return redirect('t_classroom')
            else:
                return render(request, 'landing.html')
    else:
        form = add_class_form()

    return render(request, 'teacher_classroom.html', {"form": form, "classes": classes})


def s_classroom(request):
    try:
        curr_user = Student.objects.get(user=request.user)
        classes = Classroom.objects.filter(students=curr_user)
    except Classroom.DoesNotExist:
        classes = []

    return render(request, 'student_classrooms.html', {"classes": classes})


def s_courses(request):
    curr_user = Student.objects.get(user=request.user)
    courses = Course.objects.filter(student=curr_user)
    print(courses)

    return render(request, 'student_courses.html', {"courses": courses})


def curr_classroom(request, pk, course):
    class_path = "127.0.0.1:8000/profilepage/student/classroom/" + \
        str(pk)+"/"+str(course)
    classroom = Classroom.objects.get(id=pk)
    course = Course.objects.get(id=course)
    students = Student.objects.filter(classroom__id=pk)
    if request.method == "POST":
        form = add_course_form(request.POST)
        if form.is_valid():
            chosen_courses = form.cleaned_data["courses"]
            if len(chosen_courses) > 1:
                    for i in range(len(chosen_courses)):
                        classroom.courses.add(chosen_courses[i])
            else:
                classroom.courses.add(chosen_courses[0])
    else:
        form = add_course_form()
    context = {'classroom': classroom, 'course': course,
        'students': students, 'form': form, "code": class_path}
    return render(request, 'classroom.html', context)


def add_students(request, pk):
    curr_classroom = Classroom.objects.get(id=pk)
    # print(curr_classroom)
    if request.method == 'POST':
        form = add_student_form(request.POST)

        if form.is_valid():
            student = form.cleaned_data["student_name"]

    else:
        form = add_student_form()
        student = ""

    return render(request, 'add_student.html', {"added_students": student, "form": form, "classroom": curr_classroom})


def add_students_code(request, classroomid):
    class_path = "127.0.0.1:8000/profilepage/student/classroom/add/" + \
        str(classroomid)
    courses = Course.objects.filter(classroom__id=classroomid)
    students = Student.objects.filter(classroom__id=classroomid)
    curr_classroom = Classroom.objects.get(id=classroomid)
    context = {'classroom': curr_classroom, 'courses': courses,
        'students': students, 'code': class_path}
    return render(request, 'classroom.html', context)


def add_student_to_classroom(request, pk):
    try:
        curr_student = Student.objects.get(user=request.user)
        classroom = Classroom.objects.get(id=pk)
        try:
            classroom.students.get(user=request.user)
            messages.info(request, 'Du är redan i klassrummet',
                          extra_tags="added_classroom")
            classes = Classroom.objects.filter(students=curr_student)
        except curr_student.DoesNotExist:
            print("hello?")
            classroom.students.add(curr_student)
            classroom.save()
            try:
                classes = Classroom.objects.filter(students=curr_student)
                messages.info(request, 'Du blev tillagd i klassrummet',
                              extra_tags="added_classroom")
            except Classroom.DoesNotExist:
                classes = []
                messages.info(request, 'Klassrummet fanns inte',
                              extra_tags="added_classroom")

    except Classroom.DoesNotExist:
        messages.info(request, 'Klassrummet fanns inte',
                      extra_tags="added_classroom")
        try:
            classes = Classroom.objects.filter(students=curr_student)
        except Classroom.DoesNotExist:
            classes = []

    return render(request, 'student_classrooms.html', {'classes': classes})


def remove_student(request, classroom, student):
    curr_student = Student.objects.get(id=student)
    curr_classroom = Classroom.objects.get(id=classroom)
    curr_classroom.students.remove(curr_student)
    students = Student.objects.filter(classroom__id=classroom)
    context = {'classroom': curr_classroom, 'students': students}
    return HttpResponse("")


def add_class(request):
    return render(request, 'teacher_classroom.html')


def invite_students(request):
    # change from django-invitations to own model
    # Invitation = get_invitation_model()
    # Invitation.objects.all().delete()
    # todo: Check if user already has been invited for this classroom
    # invite = Invitation.create('philip.gullberg
    # @ntig.se', inviter=request.user)
    # invite.save()
    # invite.send_invitation(request)
    return


def search_students(request, pk):
    curr_classroom = Classroom.objects.get(id=pk)
    if request.method == "POST":
        search_text = request.POST.get("search")
        result = Student.objects.filter(user__username__contains=search_text)
    else:
        result = ""
    return render(request, 'search_result.html', {'students': result, "classroom": curr_classroom})


def added(request, pk, student):
    curr_classroom = Classroom.objects.get(id=pk)
    curr_student = Student.objects.get(id=student)
    curr_classroom.students.add(curr_student)
    class_courses = Course.objects.filter(classroom__name=curr_classroom)
    for course in class_courses:
        curr_student.courses.add(course)
    message = f"Lade till {curr_student}"
    return HttpResponse("Added")


def t_results(request):
    curr_teacher = Teacher.objects.get(user=request.user)
    teachers_classrooms = Classroom.objects.filter(teacher=curr_teacher)
    classroom_courses = Course.objects.filter(classroom__teacher=curr_teacher)
    teachers_students = Student.objects.filter(classroom__teacher=curr_teacher)

    return render(request, 'teacher_results.html', {'students': teachers_students, 'classrooms': teachers_classrooms, 'courses': classroom_courses})


def t_overview(request, classid, courseid):
    curr_teacher = Teacher.objects.get(user=request.user)
    curr_classroom = Classroom.objects.get(id=classid)
    curr_course = Course.objects.get(id=courseid)
    course_chapters = Chapters.objects.filter(course=curr_course)
    course_students = Student.objects.filter(
    courses=curr_course, classroom=curr_classroom)
    visitedpages = VisitedPage.objects.all()
    videos=Videos.objects.all()
    return render(request, 't_result_overview.html', {"videos":videos,"teacher": curr_teacher, "course": curr_course, "classroom": curr_classroom, "chapters": course_chapters, "students": course_students, "visited": visitedpages})


def t_overview_s_detail(request, classid, courseid, studentid):
    curr_student = Student.objects.get(id=studentid)
    curr_class = Classroom.objects.get(id=classid)
    curr_course = Course.objects.get(id=courseid)
    course_chapters = Chapters.objects.filter(course=curr_course)
    visitedpages = VisitedPage.objects.all()
    return render(request, "t_result_s_detail.html", {"student": curr_student, "classroom": curr_class, "course": curr_course, "visited": visitedpages, "chapters": course_chapters})


def t_excercises(request):
    return render(request, "t_excercises.html")


def t_excercises_course(request, classid, courseid):
    curr_class = Classroom.objects.get(id=classid)
    curr_course = Course.objects.get(id=courseid)
    curr_teacher = Teacher.objects.get(user=request.user)

    if request.method == "POST":
        form = add_excercise_form(request.POST)
        if form.is_valid():
            chosen_excercises = form.cleaned_data["excercises"]
            chosen_deadline = form.cleaned_data["deadline"]
            subchapter = request.POST.get("subchapter")
            curr_subchapter = Subchapters.objects.get(
                subchapter_name=subchapter)

            for excercise in chosen_excercises:
                if "alla" == excercise:
                    # lägg till uppgift för alla delar
                    try:
                        curr_excercise = Quiz.objects.get(parent=curr_subchapter)
                        try:
                            excercise=Excercise.objects.get(excercise_type="Quiz", quiz_excercise=curr_excercise,
                                                subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Quiz", quiz_excercise=curr_excercise, subchapter=curr_subchapter,
                                                    classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                    
                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)

                                if curr_studentexcercise.excercises.all():
                                    for db_excercise in curr_studentexcercise.excercises.all():
                                        
                                        if excercise!=db_excercise:
                                            
                                            curr_studentexcercise.excercises.add(excercise)
                                            curr_studentexcercise.save()
                                else:
                                    curr_studentexcercise.excercises.add(excercise)
                                    curr_studentexcercise.save()
                                        
                                
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()

                    except Quiz.DoesNotExist:
                            print("doesnt exist")
                    try:
                        curr_excercise=FillInBlanks.objects.get(subchapter=curr_subchapter)
                        try:
                            excercise=Excercise.objects.get(excercise_type="Fill in blanks", fill_excercise=curr_excercise, subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Fill in blanks", fill_excercise=curr_excercise, subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)

                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                            curr_studentexcercise.excercises.add(excercise)
                                            curr_studentexcercise.save()
                                    
                                
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()
                   
                    except FillInBlanks.DoesNotExist:
                        print("doesn't exist")

                    try:
                        curr_excercise=Subchapters.objects.get(subchapter_name=subchapter)

                        try: 
                            excercise=Excercise.objects.get(excercise_type="Läs kapitel",subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Läs kapitel",subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)

                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                            curr_studentexcercise.excercises.add(excercise)
                                            curr_studentexcercise.save()
                                    
                                
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()

                    except Subchapters.DoesNotExist:
                        print("doesn't exist")


                    try:
                        curr_excercise=Videos.objects.get(parent=curr_subchapter)
                        try:
                            excercise=Excercise.objects.get(excercise_type="Se video", video_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Se video", video_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                    

                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                            curr_studentexcercise.excercises.add(excercise)
                                            curr_studentexcercise.save()
                                    
                                
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()
                            
                    
                    
                    except Videos.DoesNotExist:
                        print("doesn't exist")

                
                if "quiz"==excercise:
                    try:
                        curr_excercise=Quiz.objects.get(parent=curr_subchapter)
                        try: 
                            excercise=Excercise.objects.get(excercise_type="Quiz",quiz_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course,teacher=curr_teacher)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Quiz", quiz_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)

                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                            curr_studentexcercise.excercises.add(excercise)
                                            curr_studentexcercise.save()
                                    
                                
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()

                    except Quiz.DoesNotExist:
                        print("doesnt exist")

                if "fill in blanks"==excercise:
                    try:
                        curr_excercise=FillInBlanks.objects.get(subchapter=curr_subchapter)
                        try:
                            excercise=Excercise.objects.get(excercise_type="Fill in blanks", fill_excercise=curr_excercise, subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Fill in blanks", fill_excercise=curr_excercise, subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                    
                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                print(curr_studentexcercise.excercises.all())
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                        curr_studentexcercise.excercises.add(excercise)
                                        curr_studentexcercise.save()
                                    
                            
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()
                    
                    
                    except FillInBlanks.DoesNotExist:
                        print("doesn't exist")

                if "läs kapitlet"==excercise:
                    try:
                        curr_excercise=Subchapters.objects.get(subchapter_name=subchapter)

                        try: 
                             excercise=Excercise.objects.get(excercise_type="Läs kapitel",subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Läs kapitel",subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)

                        for curr_student in curr_class.students.all():
                            try:
                                curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                print(curr_studentexcercise.excercises.all())
                                for db_excercise in curr_studentexcercise.excercises.all():
                                    if excercise!=db_excercise:
                                         curr_studentexcercise.excercises.add(excercise)
                                         curr_studentexcercise.save()
                                    
                               
                            except StudentExcercises.DoesNotExist:
                                curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                curr_studentexcercise.excercises.add(excercise)
                                curr_studentexcercise.save()

                    except Subchapters.DoesNotExist:
                        print("doesn't exist")
                
                        
                if "se video"==excercise:
                    try:
                        curr_excercise=Videos.objects.get(parent=curr_subchapter)
                        try:
                            excercise=Excercise.objects.get(excercise_type="Se video", video_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                        except Excercise.DoesNotExist:
                            excercise=Excercise.objects.create(excercise_type="Se video", video_excercise=curr_excercise,subchapter=curr_subchapter, classroom=curr_class, course=curr_course, teacher=curr_teacher, deadline=chosen_deadline)
                    
                        for curr_student in curr_class.students.all():
                                try:
                                    curr_studentexcercise=StudentExcercises.objects.get(student=curr_student)
                                    print(curr_studentexcercise.excercises.all())
                                    for db_excercise in curr_studentexcercise.excercises.all():
                                        if excercise!=db_excercise:
                                                curr_studentexcercise.excercises.add(excercise)
                                                curr_studentexcercise.save()
                                        
                                    
                                except StudentExcercises.DoesNotExist:
                                    curr_studentexcercise=StudentExcercises.objects.create(student=curr_student)
                                    curr_studentexcercise.excercises.add(excercise)
                                    curr_studentexcercise.save()
                    
                    except Videos.DoesNotExist:
                        print("doesn't exist")
                
               
                

            return redirect("t_excercises_course",classid,courseid)
        

            
            
    else:
        form = add_excercise_form()

        return render(request, 't_excercises_course.html',{'course':curr_course,'classroom':curr_class, 'form':form})




def t_add_excercise(request):
    curr_teacher=Teacher.objects.get(user=request.user)
    if request.method == "POST":
        form = add_excercise_form(request.POST)
    else:
        form = add_excercise_form()
    return render(request,"t_add_excercise.html",{'form':form})

def t_remove_excercise(request, pk):
    Excercise.objects.get(id=pk).delete()
    return HttpResponseRedirect("")