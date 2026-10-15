from ex115a.lib.arquivo import *
from ex115a.lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opcao de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #Opcao de cadastrar nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opcao de sair do sistema
        cabecalho('SAINDO DO SISTEMA...')
        break
    else:
        #Digitou opcao errada no Menu
        print('\033[0;31mERRO: Por favor, digite um número inteiro válido!\033[m')
    sleep(1)
