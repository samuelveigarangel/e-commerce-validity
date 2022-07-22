from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    list_display_links = ['username',]
    
    fieldsets = UserAdmin.fieldsets + ((None, 
        {'fields': ('idade', 'genero', 'uf', 'estado', 'cidade', 'rua', 'telefone')}),)

    add_fieldsets = UserAdmin.fieldsets + ((None, 
        {'fields': ('idade', 'genero', 'uf', 'estado', 'cidade', 'rua', 'telefone')}),)

