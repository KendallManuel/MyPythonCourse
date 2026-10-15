def metade(n, show=False):
    """
    :param n: Preco informado
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado da metade do preco informado
    """
    resultado = n / 2
    if show:
        return moeda(resultado)
    else:
        return resultado


def dobro(n=0, show=False):
    """
    :param n: Preco informado
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado do dobro do preco informado
    """
    resultado = n * 2
    if show:
        return moeda(resultado)
    else:
        return resultado


def aumentar(n=0, a=0, show=False):
    """
    :param n: Preco informado
    :param a: A percentagem a ser aumentada
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado do aumento do preco informado.
    """
    a /= 100
    resultado = n + (n * a)
    if show:
        return moeda(resultado)
    else:
        return resultado


def diminuir(n=0, a=0, show=False):
    """
    :param n: Preco informado
    :param a: A percentagem a ser aumentada
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado do preco reduzido.
    """
    a /= 100
    resultado = n - (n * a)
    if show:
        return moeda(resultado)
    else:
        return resultado


def moeda(n=0, simbolo='R$'):
    """
    :param n: Preco informado
    :param simbolo: Definicao do simbolo
    :return: retorna a formatacao a ser usada nas funcoes: metade(), diminuir(), dobro() e aumentar().
    """
    return f'{simbolo}{n:.2f}'.replace('.', ',')


def resumo(n, a=0, d=0):
    print('-' * 35)
    print('{:*^35}'.format(' RESUMO DO VALOR '))
    print('-' * 35)
    print(f'Preco analisado: {moeda(n):>15}')
    print(f'Dobro do preco:  {dobro(n, True):>15}')
    print(f'Metade do preco: {metade(n, True):>15}')
    print(f'{a}% de aumento:   {aumentar(n, a, True):>15}')
    print(f'{d}% de reducao:   {diminuir(n, d, True):>15}')
    print('_' * 35)


"""\t - Significa tabulacao e organiza os precos em tabela."""