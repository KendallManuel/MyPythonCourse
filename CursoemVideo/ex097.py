#Programa que mostra mensagem com tamanho adaptavel
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

escreva(txt = str(input(' Digite algo: ')))