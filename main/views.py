from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'main/index.html', {'items': items})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.posted_by = request.user
            item.save()
            return redirect('home')
    else:
        form = AddPostForm()
        return render(request, 'main/add.html', {'form': form})