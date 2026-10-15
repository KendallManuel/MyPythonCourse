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