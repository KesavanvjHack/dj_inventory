from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    age = models.IntegerField(default=0)
    
    ROLE_CHOICES = [
        (0, 'Admin'),
        (1, 'Manager'),
        (2, 'Employee'),
    ]
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)