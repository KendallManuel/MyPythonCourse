from random import randint
from time import sleep
numeros = []

def sorteia(num):
    for i in range(0, 5):
        num.append(randint(0, 11))
    print('Sorteando os 5 valores da lista: ', end='')
    for i in num:
        print(f'{i}', end=' ')
        sleep(0.3)
    print("PRONTO!")

def somapar(lst):
    s = 0
    for pos in lst:
        if pos % 2 == 0:
            s += pos
    print(f"Somando os valores pares de {lst}, temos {s}")


# Programa Principal
sorteia(numeros)
somapar(numeros)
