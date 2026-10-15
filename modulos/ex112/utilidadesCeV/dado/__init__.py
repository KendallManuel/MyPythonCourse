def leiadinheiro(num):
    valido = False
    valor = 0
    while True:
        msg = str(input(num)).replace(',','.').strip()
        if msg.isalpha() or msg == '':
            print(f'\033[031mERRO: "{msg}" É UM PREÇO INVÁLIDO!\033[m')
        else:
            valor = float(msg)
            valido = True
        if valido:
            break
    return valor


