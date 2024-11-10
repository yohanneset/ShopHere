from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'main/index.html'
    context_object_name = 'items'
    paginate_by = 2
    
    def get_queryset(self):
        return Item.objects.order_by('-added_time')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'main/detail.html'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ('name', 'price', 'quantity', 'description', 'image')
    template_name = 'main/add-item.html'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ('name', 'price', 'quantity', 'description', 'image')
    template_name = 'main/add-item.html'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.posted_by


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'main/delete-item.html'
    success_url = '/'

    def test_func(self):
            item = self.get_object()
            return self.request.user == item.posted_by


class UserPostsListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'main/user-posts.html'
    context_object_name = 'items'
    paginate_by = 2

    def get_queryset(self):
        return Item.objects.filter(posted_by=self.request.user).order_by('-added_time')