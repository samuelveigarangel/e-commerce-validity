from django import template

register = template.Library()

@register.filter(name='qnt_itens_carrinho')
def qnt_itens_carrinho(product, cart):
    chaves = cart.keys()
    for id in chaves:
        if int(id) == product.id:
            return cart.get(id)    
    return 0

@register.filter(name='total_item_preco')
def total_item_preco(product, cart):
    total = 0
    for id, qnt in cart.items():
        if int(id) == product.id:
            total += qnt * product.price
    #print(total)
    return total

@register.filter(name='total_carrinho_preco')
def total_carrinho_preco(itens, cart):
    total = 0
    dict_ord = sorted(cart.items())
    dict_car = {k: v for k, v in dict_ord}
    valor_itens = list(itens.values_list('price', flat=True))

    for qnt, valor in zip(dict_car.values(), valor_itens):
        total += qnt*valor
    return total
    
@register.filter(name='qnt_total_carrinho')
def qnt_total_carrinho(cart):
    return len(cart)
