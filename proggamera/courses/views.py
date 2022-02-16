from django.shortcuts import render
from profilepage.models import *
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def course(request,courseid):
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    
    #subchapters=Subchapters.objects.filter(parent_chapter=chapters)
    print(chapters)
    print(curr_course)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters})

""" def subchapter(request,courseid, subchapterid):
    
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    subchapter=Subchapters.objects.get(id=subchapterid)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters, "subchapter": subchapter})
 """

def subchapter(request,courseid,chapterid, pageid):
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    curr_chapter=Chapters.objects.get(chapter_number=chapterid, course__id=courseid)
    subchapters=Subchapters.objects.filter(parent_chapter=curr_chapter)
    curr_student=Student.objects.get(user=request.user)
    videos=Videos.objects.filter()
    p=Paginator(subchapters,1)
    
    pageid = request.GET.get('page')
    page_obj=p.get_page(pageid)
    curr_subchapter=Subchapters.objects.get(parent_chapter=curr_chapter,subchapter_number=(int(pageid)-1))
    curr_quiz=Quiz.objects.filter(parent=curr_subchapter)
    if request.method == 'POST':
        answer_dic=list(request.POST.items())
        student_answers=[]
        student_score=[]
        #Goes through all questions and checks if students anwer is same as the right answer
        score=0
        for i in range (0,len(answer_dic)):
            if answer_dic[i][1] == answer_dic[i][0]:    
                score+=1
                student_score.append("1")
                print(student_score)
            else:
                student_score.append("0")
            student_answers.append(answer_dic[i][1])
            
        #goes through all questions and saves the result of the quiz for the curr student
        student_answers.remove(answer_dic[0][1])
        #pop the first element because it only has csrf_key inside
        del student_score[0]
        count=0
        for q in curr_quiz:
            print(student_score)
            print(student_score[count])
            if not (Quizresult.objects.filter(quiz=q,students=curr_student)):
                print("inside")
                student_result=Quizresult(quiz=q, students=curr_student, answers=student_answers[count], result=student_score[count])
                student_result.save()
                count+=1
        #implement so student can save result for specific quiz
        num_questions=len(answer_dic)-1
        return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'score':score, 'num_questions':num_questions})
    try:
        data=Quizresult.objects.filter(quiz=curr_quiz[0],students=curr_student)
        if data.exists():
            print(data[0])
            print(curr_quiz)
            for q in curr_quiz:
                print(q)
            return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'score':data[0].result, 'num_questions':len(curr_quiz)})
        else:
            return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj})
    except IndexError:
        return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj})

def next_subchapter(request, courseid, subchapterid):
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    curr_chapter_number=Subchapters.objects.filter(id=subchapterid).values("subchapter_number")
    for curr in curr_chapter_number:
        next_number=(curr['subchapter_number'])+1
    subchapter=Subchapters.objects.filter(subchapter_number=next_number,parent_chapter=chapters)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters, "subchapter": subchapter})
