def metade(n, show=False):
    resultado = n / 2
    return resultado

def dobro(n):
    resultado = n * 2
    return resultado

def aumentar(n, a=0):
    a /= 100
    resultado =  n + (n * a)
    return resultado

def diminuir(n, a=0):
    a /= 100
    resultado =  n - (n * a)
    return resultado

def moeda(n = 0, simbolo='R$'):
    return f'{simbolo}{n:.2f}'.replace('.', ',')