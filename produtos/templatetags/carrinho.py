from django import template
from produtos.models import Produto

register = template.Library()

@register.filter(name='qnt_itens_carrinho')
def qnt_itens_carrinho(produto, carrinho):
    chaves = carrinho.keys()
    for id in chaves:
        if int(id) == produto.id:
            return carrinho.get(id)    
    return 0

@register.filter(name='total_item_preco')
def total_item_preco(produto, carrinho):
    total = 0
    for id, qnt in carrinho.items():
        if int(id) == produto.id:
            total += qnt * produto.preco
    return total

@register.filter(name='total_carrinho_preco')
def total_carrinho_preco(itens, carrinho):
    preco = list()
    for i in range(len(itens)):
        preco.append(Produto.objects.values_list('preco', flat=True).get(produto_nome=itens[i]))
    
    carrrinho_list = list(carrinho.values())
    return sum([carrrinho_list[i]*preco[i] for i in range(len(itens))])

@register.filter(name='qnt_total_carrinho')
def qnt_total_carrinho(carrinho):
    return len(carrinho)
