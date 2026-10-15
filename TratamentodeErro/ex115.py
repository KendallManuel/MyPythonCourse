import leiaInt
from time import sleep
def menu():
    print('=' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    print("\033[33m[1]\033[m - \033[34mVer pessoas cadastradas\033[m"
          "\n\033[33m[2]\033[m - \033[34mCadastrar nova Pessoa\033[m"
          "\n\033[33m[3]\033[m - \033[34mSair do Sistema\033[m")
    print('=' * 40)

def mostradados(lst):
    for l in lst:
        print(f'{l["nome"]}'
              f'\t{l["idade"]:>20}anos')


def adicionadados(lst):
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = leiaInt.leiaInt(('Idade: '))
    print(f'Novo registo de {pessoas['nome']} adicionado!')
    lst.append(pessoas.copy())


#Programa Principal
pessoas = dict()
lista = [{'nome': 'Gustavo Guanabara','idade': 52},
         {'nome':'Kendall Manuel','idade': 24},
         {'nome':'Mellanie Calangue','idade': 24},
         {'nome':'Magda Carlos Moiane','idade': 48},
         {'nome':'Mason Muianga','idade': 9},
         {'nome':'Ashley Weimer','idade': 16},
         {'nome':'Kaylo Warren','idade': 13}]
while True:
    menu()
    opcao = leiaInt.leiaInt('Sua opção: ')
    print('=' * 40)
    while True:
        if opcao == 1:
            mostradados(lista)
            sleep(1.5)
            break
        elif opcao == 2:
            adicionadados(lista)
            sleep(1.5)
            break
        elif opcao == 3:
            print('=' * 40)
            print('SAINDO DO SISTEMA...'.center(40))
            print('=' * 40)
            exit()
        else:
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido!\033[m')
            break