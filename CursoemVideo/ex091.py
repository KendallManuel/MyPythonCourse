from random import randint
from time import sleep
from operator import itemgetter
Team = dict()
print("Valores sorteados:")
for i in range(0, 3):
    Team["jogador1"] = randint(1, 6)
    Team["jogador2"] = randint(1, 6)
    Team["jogador3"] = randint(1, 6)
    Team["jogador4"] = randint(1, 6)
ranking = []
for ky, val in Team.items():
    print(f"O {ky} tirou {val} no dado.")
    sleep(1)
ranking = sorted(Team.items(), key=itemgetter(1), reverse=True) #itemgetter serve para colocar os elementos em ordem crescente. Tanto para as keys, assim como para os values de um dicionario.
print("«»"*20)
print(" ==RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"    {i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)
