from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Lojista


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["id", "email", "username"]
    list_display_links = ["username", "email"]

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    fieldsets = UserAdmin.fieldsets + (("Role", {"fields": ("role",)}),)


@admin.register(Lojista)
class LojistaAdmin(admin.ModelAdmin):
    list_display = [
        "supermarket",
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(LojistaAdmin, self).get_form(request, obj=None, **kwargs)
        form.base_fields["supermarket"].queryset = CustomUser.objects.filter(
            role="SUPERMARKET"
        )
        return form


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     pass
