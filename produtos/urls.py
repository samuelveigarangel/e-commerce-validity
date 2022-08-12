from django.urls import path
from .views import ProcurarProdutosList, ProdutosDetail, OrdemView, HomeView, CheckoutView

app_name = 'produtos'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('result/', ProcurarProdutosList.as_view(), name='procurar_produto'),
    path('produto/<slug:slug>', ProdutosDetail.as_view(), name='produto_detail'),
    path('carrinho/', OrdemView.as_view(), name='ordemview'),
    path('finalizar/', CheckoutView.as_view(), name='finalizar')
]