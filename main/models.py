from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/images/', default='products/images/default.jpg')
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    added_time = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')