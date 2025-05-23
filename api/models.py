from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUSES = [
    ('TBD', 'To be done'),
    ('IP', 'In Progress'),
    ('D', 'Done')
]

class User(AbstractUser):
    pass

class Task(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUSES)
    #creator = models.ForeignKey(User, on_delete=models.CASCADE)