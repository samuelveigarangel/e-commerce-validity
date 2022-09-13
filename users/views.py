from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Ordem


class MinhasCompras(ListView):
    model = Ordem
    context_object_name = "ordens"
    template_name = "users/minhas_compras.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
