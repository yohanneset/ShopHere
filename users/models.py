from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    male, female = 'M', 'F'
    choice = {
        male : 'Male',
        female: 'Female'
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1,choices=choice)

    
    def __str__(self) -> str:
        return self.user.username

