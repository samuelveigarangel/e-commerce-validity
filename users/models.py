from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username


