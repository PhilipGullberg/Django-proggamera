from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('teacher/', views.teacherdash, name="teacher_dash"),
    path('student/', views.studentdash, name="student_dash"),
    path('student/classroom', views.s_classroom, name="s_classroom"),
    path('student/courses', views.s_courses, name="s_courses"),
    path('teacher/classroom/', views.t_classroom, name="t_classroom"),
    path('teacher/results',views.t_results, name="t_results"),
    path('teacher/classroom/<int:pk>', views.curr_classroom, name="curr_classroom"),
    path('teacher/classroom/<int:pk>/add', views.add_students, name="add_students"),
    path('teacher/classroom/<int:pk>/search_students/', views.search_students, name="search_students"),
    path('teacher/classroom/<int:pk>/search_students/added/<int:student>', views.added, name="added"),
    path('teacher/classroom/<int:classroom>/<str:student>', views.remove_student , name="remove_student"),
    


]
htmx_urlpatterns = [
    #path('search_students', views.search_students, name="search_students"),

]
urlpatterns+=htmx_urlpatterns
 
