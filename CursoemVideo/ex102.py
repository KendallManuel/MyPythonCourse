def fatorial(n=1, show=False):
    """
    => Calcula o factorial de um numero natural.
    :param n: O numero a ser calculado.
    :param show: Para mostrar ou nao o calculo (Opcional).
    :return: Para retornar o resultado da conta.
    Criado por Kendall Manuel...
    """
    c = n
    f = 1
    while c > 0:
        if show:
            print(f'{c}', end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c
        c -= 1
    return f


#Programa Principal
print('=' * 25)
print(fatorial(5, True))
print('=' * 25)

help(fatorial)