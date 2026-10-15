def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0

#Programa Principal
n1 = leiaInt('Digite um nº. inteiro: ')
n2 = leiaFloat('Digite um nº. real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')
