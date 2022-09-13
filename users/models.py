from secrets import choice
from django.contrib.auth.models import AbstractUser
from django.db import models

from localflavor.br.models import BRPostalCodeField
from localflavor.br import br_states

from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SUPERMARKET = "SUPERMARKET", _("Supermarket")
        CLIENT = "CLIENT", _("Client")

    role = models.CharField(max_length=50, choices=Role.choices)

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Lojista(models.Model):
    def upload_photo_to(instance, filename):
        return f"brand/{instance.name}/{filename}"

    supermarket = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True
    )
    brand = models.ImageField(upload_to=upload_photo_to, blank=True, null=True)
    cep = BRPostalCodeField()
    state = models.CharField(choices=br_states.STATE_CHOICES, max_length=2, null=False)
    city = models.CharField(max_length=128, null=False)
    district = models.CharField(max_length=128, null=True)
    street = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.supermarket.username} - {self.street}, {self.district} - {self.city}/{self.state}"
