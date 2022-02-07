from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
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
            user=form.save()
            user_type=form.cleaned_data.get('user_type')
            if user_type =="T":
                user.is_teacher=True
            else:
                user.is_student=True
            user.save()

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