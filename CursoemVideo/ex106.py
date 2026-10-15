from time import sleep
cores = [
        '\033[m',        # 0 - sem cor
        '\033[0;30;41m',    # 1 - vermelho
        '\033[0;30;42m',    # 2 - verde
        '\033[0;33m',    # 3 - amarelo
        '\033[0;34m',    # 4 - azul
        '\033[0;35m',    # 5 - roxo
        '\033[0;36m',    # 6 - ciano
        '\033[0;30;47m'     # 7 - cinza
    ]
def display(msg, cor=0):
    print(cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(cores[0], end='')
    return msg


# Programa Principal
while True:
    sleep(0.5)
    txt = 'SISTEMA DE AJUDA PyHELP'
    display(txt, 2)
    func = str(input('Funcao ou Biblioteca > '))
    fim = 'ATE LOGO!'
    if func in 'quit':
        break
    sleep(1)
    info = "Acessando o manual do comando '{}'".format(func)
    display(info,4)
    sleep(1)
    print(cores[7], end='')
    help(func)
    print(cores[7], end='')
display(fim,1)