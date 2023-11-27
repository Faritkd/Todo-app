from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
