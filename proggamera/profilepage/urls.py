from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('teacher/', views.teacherdash, name="teacher_dash"),
    path('student/', views.studentdash, name="student_dash"),
    path('student/classroom', views.s_classroom, name="s_classroom"),
    path('student/classroom/add/<int:pk>',views.add_student_to_classroom, name="student_code"),
    path('student/courses', views.s_courses, name="s_courses"),
    path('teacher/classroom/', views.t_classroom, name="t_classroom"),
    path('teacher/excercises/', views.t_excercises, name="t_excercises"),
    path('teacher/excercises/add', views.t_add_excercise, name="t_add_excercise"),
    path('teacher/results',views.t_results, name="t_results"),
    path('teacher/results/<int:classid>/<int:courseid>/overview',views.t_overview, name="result_overview"),
    path('teacher/results/<int:classid>/<int:courseid>/overview/<int:studentid>/studentdetail',views.t_overview_s_detail, name="result_detail"),
    path('teacher/classroom/<int:pk>/<int:course>/', views.curr_classroom, name="curr_classroom"),
    path('teacher/classroom/<int:pk>/add', views.add_students, name="add_students"),
    path('teacher/classroom/<int:classroomid>/add/code', views.add_students_code, name="add_students_code"),
    path('teacher/classroom/<int:pk>/search_students/', views.search_students, name="search_students"),
    path('teacher/classroom/<int:pk>/search_students/added/<int:student>', views.added, name="added"),
    path('teacher/classroom/remove/<int:classroom>/<str:student>', views.remove_student , name="remove_student"),
]
