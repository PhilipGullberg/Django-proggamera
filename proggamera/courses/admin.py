from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Videos)
admin.site.register(Quiz)
admin.site.register(Quizresult)
admin.site.register(FillInBlanks)
admin.site.register(FillInBlanksResults)
admin.site.register(VisitedPage)
admin.site.register(VideoWatched)