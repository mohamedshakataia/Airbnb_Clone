from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UseCreateForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username' , 'email' , 'password1' , 'password2']



class userform(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['username' , 'email' , 'first_name' , 'last_name']



class Profileform(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = ['image' , 'phone_number' , 'address']

