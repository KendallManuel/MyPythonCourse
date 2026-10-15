from time import sleep
def contador(inicio, fim, passo):
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


#Programa Principal
print('a) De 1 até 10, de 1 em 1: ', end=' ')
contador(1, 10, 1 )
print('b) De 10 até 0, de 2 em 2: ', end=' ')
contador(10, -2, -2)
print('c) Contagem personalizada.')
contador(inicio = int(input('Digite o inicio: ')),
         fim = int(input('Digite o fim: ')),
         passo = int(input('Digite o passo: ')))
