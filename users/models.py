from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    idade = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    rua = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    

    def __str__(self):
        return self.username


