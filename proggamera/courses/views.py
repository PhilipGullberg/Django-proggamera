from django.shortcuts import render
from profilepage.models import *
from django.core.paginator import Paginator

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
    curr_chapter=Chapters.objects.get(id=chapterid)
    subchapters=Subchapters.objects.filter(parent_chapter=curr_chapter)
    videos=Videos.objects.filter()
    p=Paginator(subchapters,1)
    
    pageid = request.GET.get('page')
    page_obj=p.get_page(pageid)
    
    return render(request,"course.html", {"course":curr_course,"chapters":chapters, "page_obj": page_obj})
 
def next_subchapter(request, courseid, subchapterid):
    curr_course=Course.objects.get(id=courseid)
    chapters=Chapters.objects.filter(course=curr_course)
    curr_chapter_number=Subchapters.objects.filter(id=subchapterid).values("subchapter_number")
    for curr in curr_chapter_number:
        next_number=(curr['subchapter_number'])+1
    subchapter=Subchapters.objects.filter(subchapter_number=next_number,parent_chapter=chapters)
    return render(request,"course.html", {"course":curr_course,"chapters":chapters, "subchapter": subchapter})
