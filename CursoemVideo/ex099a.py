from time import sleep

def maior(*num):
    cont = mai = 0
    print('-=' * 20)
    print(f'Analizando os valores...')
    for i in num:
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            mai = i
        else:
            if i > mai:
                mai = i
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior e {mai}.')


# Programa Principal
maior(5, 9, 7, 0, 5, 1)
maior(3, 2, 1)
maior(2, 7, 8, 10)
maior(7)
maior()