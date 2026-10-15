def linha():
    print('\033[35m-=\033[m' * 20)

def leiaInt(num):
    valor = 0
    valido = False
    msg = ''
    while True:
        try:
            msg = str(input(num))
            if msg.isnumeric():
                valor = int(msg)
                valido = True
            else:
                print('\033[0;31mERRO: Por favor, digite um número inteiro válido!\033[m')
            if valido:
                break
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            break
    return valor


def leiaFloat(num):
    valido = False
    valor = 0
    msg = str
    while not valido:
        try:
            msg = str(input(num)).replace(',','.').strip()
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            break
        else:
            if msg.isalpha() or msg == '':
                print('\033[0;31mERRO: Por favor, digite um número real válido!\033[m')
            else:
                try:
                    valor = float(msg)
                    valido = True
                except ValueError:
                    print('\033[31mERRO: Por favor, digite um número real válido!\033[m')
    return valor


#Programa Principal
linha()
numero = leiaInt('\033[36mDigite um nº. inteiro: \033[m')
real = leiaFloat('\033[36mDigite um nº. real: \033[m')
linha()
print(f'\033[32mO valor inteiro digitado foi {numero} e o real foi {real:.2f} .\033[m')
