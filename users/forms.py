from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = True
        self.fields['username'].help_text = False
    #nomes padroes em uma unica linguagem
    class Meta:
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'idade',  'telefone')

        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'idade', 'telefone')