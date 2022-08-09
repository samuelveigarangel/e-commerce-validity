def diminui_carrinho(carrinho, produto, quantidade):
    if quantidade != 1:
        pass


def aumenta_carrinho(carrinho, produto, quantidade):
    carrinho[produto] = quantidade + 1


def remove_carrinho(*args):
    del args[0][args[1]]
    # del carrinho[produto]


def carrinho_acoes(carrinho, produto, quantidade, op):
    acoes = {
        '-': diminui_carrinho,
        '+': aumenta_carrinho,
        'rmv': remove_carrinho
    }
    try:
        return acoes[str(op)](carrinho, produto, quantidade)
    except KeyError:
        print('Key invalido')