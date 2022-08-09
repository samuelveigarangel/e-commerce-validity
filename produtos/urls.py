from django.urls import path
from .views import ProcurarProdutosList, ProdutosDetail, OrdemView

app_name = 'produtos'

urlpatterns = [
    path('', ProcurarProdutosList.as_view(), name='procurar_produto'),
    path('<slug:slug>', ProdutosDetail.as_view(), name='produto_detail'),
    path('carrinho/', OrdemView.as_view(), name='ordemview'),
]