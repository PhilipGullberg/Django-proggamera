from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from profilepage.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            curr_user=form.save()
            user_type=form.cleaned_data.get('user_type')
            if user_type =="T":
                curr_user.is_teacher=True
                curr_user.save()
                add_teacher=Teacher(user=curr_user)
                add_teacher.save()
            else:
                curr_user.is_student=True
                curr_user.save()
                add_student=Student(user=curr_user)
                add_student.save()
            

            messages.success(request, 'Account was created for ')
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})

def login_req(request):
    print(request)
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('landing')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, 'login.html',{'form':form})


def logout_req(request):
    logout(request)
    return redirect('landing')