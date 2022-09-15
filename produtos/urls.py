from django.urls import path
from .views import (
    ProcurarProdutoView,
    ProdutoDetail,
    OrdemView,
    HomeView,
    CheckoutView,
    CategoriaProdutoView,
)

app_name = "produtos"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("result/", ProcurarProdutoView.as_view(), name="procurar_produto"),
    path("produto/<slug:slug>", ProdutoDetail.as_view(), name="produto_detail"),
    path("carrinho/", CheckoutView.as_view(), name="ordemview"),
    path("finalizar/", OrdemView.as_view(), name="finalizar"),
    path("categoria/<slug:slug>", CategoriaProdutoView.as_view(), name="categoria"),
]
