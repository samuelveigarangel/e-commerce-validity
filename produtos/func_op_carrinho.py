def diminui_carrinho(cart, product, quantity):
    if quantity != 1:
        cart[product] = quantity - 1


def aumenta_carrinho(cart, product, quantity):
    cart[product] = quantity + 1


def remove_carrinho(*args):
    del args[0][args[1]]
    # del cart[product]


def carrinho_acoes(cart, product, quantity, op):
    acoes = {
        '-': diminui_carrinho,
        '+': aumenta_carrinho,
        'rmv': remove_carrinho
    }
    try:
        return acoes[str(op)](cart, product, quantity)
    except KeyError:
        print('Key invalido')