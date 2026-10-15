def leiaInt(num):
    ok = False
    valor = 0
    while True:
        msg = str(input(num))
        if msg.isnumeric():
            valor = int(msg)
            ok = True
        else:
            print('\033[031mERRO! DIGITE UM VALOR INTEIRO VALIDO.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')
