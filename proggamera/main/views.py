from django.shortcuts import render
from user.models import CustomUser

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        if request.user.is_teacher or request.user.is_student:
            print(request.user.is_teacher)
            print("teacher or student")
            return render(request, "landing.html")
        else:
            no_role=True
            
            return render(request, "landing.html",{"no_role":no_role})
    else:
        return render(request, "landing.html")