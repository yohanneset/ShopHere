from django import forms
from .models import Item

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'quantity', 'description']
