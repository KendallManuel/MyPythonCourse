def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3


#Programa Principal
num = int(input('Digite umnumero: '))
fat = fatorial(num)
print(f'O factorial de {num} e {fat}')
print(f'O dobro de {num} e {dobro(num)}')
print(f'O triplo de {num} e {triplo(num)}')