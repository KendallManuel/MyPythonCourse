
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

def dobro(n, show=False):
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

def aumentar(n, a=0, show=False):
    """

    :param n: Preco informado
    :param a: A percentagem a ser aumentada
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado do aumento do preco informado.
    """
    a /= 100
    resultado =  n + (n * a)
    if show:
        return moeda(resultado)
    else:
        return resultado

def diminuir(n, a=0, show=False):
    """

    :param n: Preco informado
    :param a: A percentagem a ser aumentada
    :param show: Mostra/Oculta simbolo de moeda
    :return: retorna o resultado do preco reduzido.
    """
    a /= 100
    resultado =  n - (n * a)
    if show:
        return moeda(resultado)
    else:
        return resultado

def moeda(n = 0, simbolo='R$'):
    """

    :param n: Preco informado
    :param simbolo: Definicao do simbolo
    :return: retorna a formatacao a ser usada nas funcoes: metade(), diminuir(), dobro() e aumentar().
    """
    return f'{simbolo}{n:.2f}'.replace('.', ',')
