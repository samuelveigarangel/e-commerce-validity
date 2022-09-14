from produtos.models import Ordem
from .models import  CustomUser

from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import  LoginRequiredMixin

class MinhasCompras(LoginRequiredMixin, ListView):
    model = Ordem
    context_object_name = "ordens"
    template_name = "users/minhas_compras.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class Perfil(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/perfil.html'
    fields = ['username', 'first_name', 'last_name', 'email']