from ast import Or
from django.shortcuts import redirect, render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Produto, OrdemItem, Ordem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

from .func_op_carrinho import carrinho_acoes
from .random_number import random_number
# Create your views here.

class HomeView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'home.html'


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



    def post(self, request, *args, **kwargs):
        produto = str(self.get_object().id)
        carrinho = request.session.get('carrinho')

        if carrinho:
            quantidade = carrinho.get(produto)
            if quantidade:
                carrinho[produto] = quantidade + 1  
            else:
                carrinho[produto] = 1
        else:
            carrinho = {}
            carrinho[produto] = 1


        request.session['carrinho'] = carrinho
        
        return redirect('produtos:ordemview')


class OrdemView(View):

    def get(self, request):
        try:
            produto = Produto.objects.filter(id__in=list(request.session.get('carrinho').keys()))                       
            context = {
                'itens': produto
            }
            return render(request, 'produto/carrinho.html', context)
        except ObjectDoesNotExist:
            return render(request, 'produto/carrinho.html', {})
        except:
            return render(request, 'produto/carrinho.html', {})


    def post(self, request):
        produto = request.POST.get('id')
        carrinho = request.session.get('carrinho')
        op_quantidade = request.POST.get('alt_quantidade')
        del_car = request.POST.get('del_carrinho')

        if del_car:
            del request.session['carrinho']
            return redirect('produtos:ordemview') 

        if carrinho:
            quantidade = carrinho.get(produto)
            if quantidade:
                carrinho_acoes(carrinho, produto, quantidade, op_quantidade)
            else:
                carrinho[produto] = 1
        else:
            carrinho = {}
            carrinho[produto] = 1
        
        request.session['carrinho'] = carrinho
       

        return redirect('produtos:ordemview')

class CheckoutView(LoginRequiredMixin, View):

    def get(self, request):
        # print(request.session.get('carrinho'))
        try:
            product = Produto.objects.filter(id__in=list(request.session.get('carrinho').keys()))
            
            dict_ord = sorted(request.session['carrinho'].items())
            dict_car = {k: v for k, v in dict_ord}
        
            order, created = Ordem.objects.get_or_create(user=request.user, enviado=False)
            itens = []
            
            for prod, qnt in zip(product, dict_car.values()):
                order_item, created = OrdemItem.objects.get_or_create(produto=prod, ordem=order, quantidade=qnt)
                itens.append(order_item)
            
            del request.session['carrinho']
            
            order.enviado = True
            order.save()

            context = {
                'itens': itens
            }

            return render(request, 'produto/checkout.html', context)
        except ObjectDoesNotExist:
            return redirect('produtos:home')
        except Exception as e:
            print(e)
            return redirect('produtos:home')