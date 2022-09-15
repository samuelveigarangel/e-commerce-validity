from itertools import product
from django.views.generic import ListView, UpdateView, CreateView
from produtos.models import Produto, Ordem
from users.models import Lojista
from .forms import CriarProdutoForms

from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse


class SupermarketUserMixin(UserPassesTestMixin, LoginRequiredMixin):
    def test_func(self):
        if self.request.user.is_authenticated:
            print("entrou")
            print(self.request.user.role)
            return (
                self.request.user.role == "SUPERMARKET"
                or self.request.user.is_superuser
            )

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'Entre com um usuário SUPERMARKET')
        return redirect("login")


class MinhasOrdens(SupermarketUserMixin, ListView):
    model = Ordem
    template_name = "lojista/minhas_ordens.html"
    context_object_name = "orders"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(supermarket__supermarket=self.request.user)


class MeusProdutos(SupermarketUserMixin, ListView):
    model = Produto
    template_name = "lojista/produtos.html"
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(supermarket__supermarket=self.request.user)


class EditProduct(SupermarketUserMixin, UpdateView):
    model = Produto
    template_name = "lojista/editar_produto.html"
    context_object_name = "products"
    success_url = reverse_lazy("lojista:minhas_ordens")
    fields = [
        "name",
        "price",
        "qnt_stock",
        "sold",
        "category",
        "description",
        "image",
        "expiration_date",
    ]


class CriarProduto(SupermarketUserMixin, CreateView):
    model = Produto
    form_class = CriarProdutoForms
    template_name = "lojista/criar_produto.html"
    success_url = reverse_lazy("lojista:meus_produtos")

    def form_valid(self, form):
        form.instance.supermarket = get_object_or_404(
            Lojista, supermarket=self.request.user
        )
        return super().form_valid(form)


def delete_produto(request, pk):
    product = get_object_or_404(Produto, pk=pk)
    product.delete()
    return redirect("lojista:meus_produtos")
