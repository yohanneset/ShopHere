from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            profile = Profile.objects.get(user=user)
            profile.age = age
            profile.gender = gender
            profile.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} created account successfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form' : form })


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')