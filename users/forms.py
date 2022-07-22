from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
    #nomes padroes em uma unica linguagem
    class Meta:
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'idade', 'genero', 'uf', 'estado', 'cidade', 'rua', 'telefone')

        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'idade', 'genero', 'uf', 'estado', 'cidade', 'rua', 'telefone')