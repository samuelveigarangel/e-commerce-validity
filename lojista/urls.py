from django.urls import path
from .views import MeusProdutos, EditProduct, MinhasOrdens, CriarProduto, delete_produto

app_name = "lojista"

urlpatterns = [
    path("criar-produto/", CriarProduto.as_view(), name="criar_produto"),
    path("", MinhasOrdens.as_view(), name="minhas_ordens"),
    path("meus-produtos/", MeusProdutos.as_view(), name="meus_produtos"),
    path("<int:pk>/", EditProduct.as_view(), name="editar_produto"),
    path("deleta/<int:pk>/", delete_produto, name="deletar_produto"),
]
