from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=245,null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    texts = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texts



