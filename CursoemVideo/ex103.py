def ficha(n= '', g=0):
    print(f'O jogador {n} marcou {g} gol(s).')

#Programa Principal
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
if nome == '':
    nome = '<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
