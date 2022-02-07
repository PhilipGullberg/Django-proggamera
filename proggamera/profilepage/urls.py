from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('teacher/', views.teacherdash, name="teacher_dash"),
    path('student/', views.studentdash, name="student_dash"),
    path('teacher/classroom/', views.t_classroom, name="t_classroom"),
    path('teacher/classroom/<int:pk>', views.curr_classroom, name="curr_classroom"),
    path('teacher/classroom/<int:pk>', views.add_students, name="add_students"),
    path('teacher/classroom/<int:classroom>/<str:student>', views.remove_student , name="remove_student"),
    


]
htmx_urlpatterns = [
    path('search_students', views.search_students, name="search_students"),

]
urlpatterns+=htmx_urlpatterns
 
