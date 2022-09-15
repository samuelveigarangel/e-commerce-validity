from produtos.models import Ordem
from .models import CustomUser
from .forms import UpdateForm

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MinhasCompras(LoginRequiredMixin, ListView):
    model = Ordem
    context_object_name = "ordens"
    template_name = "users/minhas_compras.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).order_by('-order_date')


class Perfil(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "users/perfil.html"
    form_class = UpdateForm

    def get_success_url(self):
        userid = self.kwargs["pk"]
        return reverse_lazy("users:perfil", kwargs={"pk": userid})
