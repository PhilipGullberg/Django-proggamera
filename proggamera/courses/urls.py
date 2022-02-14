from django.urls import path
from . import views

urlpatterns = [
    path('course/<str:courseid>', views.course, name="courses"),
    path('course/<str:courseid>/chapter/<str:chapterid>/subchapter/<str:pageid>/', views.subchapter, name="subchapter"),
    path('course/<str:courseid>/subchapter/<str:subchapterid>/next', views.next_subchapter, name="nextsubchapter"),
]