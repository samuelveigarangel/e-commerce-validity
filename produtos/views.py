from typing import List
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView
from .models import Produto

# Create your views here.

class ProcurarProdutosList(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'produtos'
    paginate_by = 10

    def get_queryset(self):
        txt_pesquisa = self.request.GET.get('pesquisar_produto')

        if txt_pesquisa:
            produto = Produto.objects.filter(produto_nome__icontains=txt_pesquisa.strip()).order_by('produto_nome')
        else:
            produto = Produto.objects.none()
        
        return produto
    

class ProdutosDetail(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
    context_object_name = 'produto'


class CarrinhoView(TemplateView):
    template_name = 'produto/carrinho.html'
