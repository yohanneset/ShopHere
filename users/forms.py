from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    male, female = 'M', 'F'
    choice = {
        male : 'Male',
        female: 'Female'
    }
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=choice)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'age', 'gender')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'image']

