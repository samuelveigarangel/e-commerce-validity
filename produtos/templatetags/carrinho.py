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
    #print(total)
    return total

@register.filter(name='total_carrinho_preco')
def total_carrinho_preco(itens, carrinho):
    total = 0
    dict_ord = sorted(carrinho.items())
    dict_car = {k: v for k, v in dict_ord}
    valor_itens = list(itens.values_list('preco', flat=True))
    
    for qnt, valor in zip(dict_car.values(), valor_itens):
        total += qnt*valor
    return total
    
@register.filter(name='qnt_total_carrinho')
def qnt_total_carrinho(carrinho):
    return len(carrinho)
