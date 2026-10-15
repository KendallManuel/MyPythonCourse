from ex115a.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        # rt - significa read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        # wt+ - siginifica write 'criar' text. '+' cria se nao existir.
        a.close()
    except:
        print('Houve um ERRO na criacao de arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>8}anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
        # at - significa append text (adicionar texto).
    except:
        print('Houve um ERRO na abertura de arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO no momento de escrita de dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()