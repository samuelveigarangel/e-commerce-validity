from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import transaction

from .models import CustomUser, Client


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = True
        self.fields["username"].help_text = False

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    @transaction.atomic
    def save(self):
        user = super().save()
        user.role = CustomUser.Role.CLIENT
        user.save()
        client = Client.objects.create(user=user)
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]

    email = forms.CharField(disabled=True)
