from msilib.schema import Class
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Chapters)
admin.site.register(Subchapters)