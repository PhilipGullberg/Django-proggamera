from django.shortcuts import render
from user.models import CustomUser

# Create your views here.
def landing(request):
    
    if request.user.is_authenticated:
        if request.user.is_teacher or request.user.is_student:
            if request.user.is_teacher:
                user_type="Teacher"
                
                return render(request, "landing.html",{"user_type":user_type})
            else:
                user_type="Student"
                
                return render(request, "landing.html",{"user_type":user_type})  
        else:
            no_role=True
            
            
        return render(request, "landing.html",{"no_role":no_role})
    else:
        return render(request, "landing.html")
    
