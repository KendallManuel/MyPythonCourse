def linhas(l):
    x = len(l)
    print('-=' * x)
    print(f'    \t{l}')
    print('-=' * x)

def tenteconectar(msg):
    import urllib
    from urllib import request, error
    try:
        site = request.urlopen(f'http://{msg}')
    except urllib.error.URLError:
        print(f'\n\033[1;31mO site não está disponível no momento.\033[m')
    else:
        print(f'\n\033[1;34mO site está acessivel!\033[m')
        print(site.read().decode('utf-8'))
    finally:
        print('-=' * 16)
        print('Programa Encerrado!')


linhas('TESTE DE CONEXAO')
tenteconectar(str(input('Site para avaliar: ')))