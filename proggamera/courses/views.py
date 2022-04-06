from queue import Empty
from django.shortcuts import redirect, render
from profilepage.models import *
from django.core.paginator import Paginator
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def course(request,courseid):
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    
    #subchapters=Subchapters.objects.filter(parent_chapter=chapters)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters})

""" def subchapter(request,courseid, subchapterid):
    
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    subchapter=Subchapters.objects.get(id=subchapterid)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters, "subchapter": subchapter})
 """

def subchapter(request,courseid,chapterid, pageid):
    curr_student=Student.objects.get(user=request.user)
    
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    curr_chapter=Chapters.objects.get(chapter_number=chapterid, course__id=courseid)
    subchapters=Subchapters.objects.filter(parent_chapter=curr_chapter)
    
    videos=Videos.objects.filter()
    p=Paginator(subchapters,1)
    
    pageid = request.GET.get('page')
    page_obj=p.get_page(pageid)
    if(pageid):
        curr_subchapter=Subchapters.objects.get(parent_chapter=curr_chapter,subchapter_number=(int(pageid)-1))
    else:
        curr_subchapter=Subchapters.objects.get(parent_chapter=curr_chapter,subchapter_number=(1))

    if not VisitedPage.objects.filter(student=curr_student, subchapter=curr_subchapter).exists():
        VisitedPage(student=curr_student,page=request.build_absolute_uri(), visited=True, subchapter=curr_subchapter).save()

    curr_fillblanks= FillInBlanks.objects.filter(subchapter=curr_subchapter)
    try:
        student_fill_result=FillInBlanksResults.objects.filter(parent=curr_fillblanks[0],student=curr_student)
    except IndexError:
        student_fill_result=[]

    curr_quiz=Quiz.objects.filter(parent=curr_subchapter)
    if request.method == 'POST':
        answer_dic=list(request.POST.items())

        #code for fill_in_blanks post:
        for i in range (0,len(answer_dic)):
            if(answer_dic[i][0]=="user_input"):
                curr_student_fill_result=FillInBlanksResults.objects.filter(parent=curr_fillblanks[0],student=curr_student)
                if answer_dic[i][1]==curr_fillblanks[0].answer:
                    if not curr_student_fill_result:
                        curr_student_fill_result=FillInBlanksResults(parent=curr_fillblanks[0],student=curr_student,answer=answer_dic[i][1],result=1 )
                        curr_student_fill_result.save()
                    else:
                        if answer_dic[i][1] != curr_student_fill_result[0].answer:
                            curr_student_fill_result.update(answer=answer_dic[i][1], result=1)
                    
                    return render(request, "fill_in_results.html",{'fill_in_blanks':curr_fillblanks,"student_fill_result":curr_student_fill_result})
                else:
                    if not curr_student_fill_result:
                        curr_student_fill_result=FillInBlanksResults(parent=curr_fillblanks[0],student=curr_student,answer=answer_dic[i][1],result=0 )
                        curr_student_fill_result.save()
                    else:
                        curr_student_fill_result=FillInBlanksResults.objects.filter(parent=curr_fillblanks[0],student=curr_student)
                        if answer_dic[i][1] != curr_student_fill_result[0].answer:
                            curr_student_fill_result.update(answer=answer_dic[i][1], result=0)
                    

                    return render(request, "fill_in_results.html",{'fill_in_blanks':curr_fillblanks,"student_fill_result":curr_student_fill_result})
        student_answers=[]
        student_score=[]
        #Goes through all questions and checks if students anwer is same as the right answer
        score=0
        for i in range (0,len(answer_dic)):
            if answer_dic[i][1] == answer_dic[i][0]:    
                score+=1
                student_score.append("1")
            else:
                student_score.append("0")
            student_answers.append(answer_dic[i][1])
            
        #goes through all questions and saves the result of the quiz for the curr student
        student_answers.remove(answer_dic[0][1])
        #pop the first element because it only has csrf_key inside
        del student_score[0]
        count=0
        for q in curr_quiz:
            if not (Quizresult.objects.filter(quiz=q,students=curr_student)):
                student_result=Quizresult(quiz=q, students=curr_student, answers=student_answers[count], result=student_score[count])
                student_result.save()
                count+=1
        #implement so student can save result for specific quiz
        num_questions=len(answer_dic)-1
        return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'score':score, 'num_questions':num_questions,'fill_in_blanks':curr_fillblanks,"student_fill_result":student_fill_result})
    try:
        data=Quizresult.objects.filter(quiz=curr_quiz[0],students=curr_student)
        if data.exists():
            return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'score':data[0].result, 'num_questions':len(curr_quiz),'fill_in_blanks':curr_fillblanks,"student_fill_result":student_fill_result})
        else:
            return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'fill_in_blanks':curr_fillblanks,"student_fill_result":student_fill_result})
    except IndexError:
        return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj,'fill_in_blanks':curr_fillblanks,"student_fill_result":student_fill_result})

def timer(request, videoid):
    data=list(request.POST.items())
    curr_student=Student.objects.get(user=request.user)
    curr_video=Videos.objects.get(id=videoid)
    student_watchtime=int(data[0][1])
    url=data[0][0]
    try: 
        videowatch=VideoWatched.objects.get(video=curr_video, student=curr_student)
        videowatch.watched=True
        videowatch.watchtime+=student_watchtime
        videowatch.save()

    except ObjectDoesNotExist:
        new_watchtime=VideoWatched(student=curr_student, video=curr_video, watched=True, watchtime=student_watchtime)
        new_watchtime.save()
    return redirect(url)