from django.urls import path
from .views import ProcurarProdutosList, ProdutosDetail, CarrinhoView

app_name = 'produto'

urlpatterns = [
    path('', ProcurarProdutosList.as_view(), name='procurar_produto'),
    path('<slug:slug>', ProdutosDetail.as_view(), name='produto_detail'),
    path('carrinho/<slug>/', CarrinhoView.as_view(), name='carrinho'),
]