from django.urls import path
from .views import home, add_post

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_post, name='add-post'),
]