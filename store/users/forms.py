from dataclasses import fields
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# captcha
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
