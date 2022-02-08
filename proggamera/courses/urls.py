from django.urls import path
from . import views

urlpatterns = [
    path('course/<str:courseid>', views.course, name="courses"),
]