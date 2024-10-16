from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
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
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Profile is successfully updated')
            return redirect('profile')
        else:
            messages.error('please the errors below')
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'users/profile.html', context)