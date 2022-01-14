from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
    max_length=100,
    required = True,
    help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter First Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
    max_length=200,
    required = True,
    help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
    help_text='Enter Password',
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
    required = True,
    help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    types=[( "S", "Student"),("T","Teacher")]
    user_type = forms.CharField(required = True,widget=forms.Select(choices=types))
    
    class Meta:
        model = CustomUser
        fields = [
        'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'user_type',
        ]
    
