from django.urls import path,re_path
from . import views

urlpatterns = [
    path('course/<str:courseid>/chapter/1/subchapter/1', views.course, name="courses"),
    path('course/<str:courseid>/chapter/<str:chapterid>/subchapter/<str:pageid>/', views.subchapter, name="subchapter"),
    path('course/<str:videoid>', views.timer, name="timer"), 


]