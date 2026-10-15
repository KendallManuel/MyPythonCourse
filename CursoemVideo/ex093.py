#Programa que gerencia o aproveitamento de um jogador de futebol.
jogador = dict()
golos = []
tot = 0
jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(0, partidas):
    golos.append(int(input(f"Quantos golos na partida {i}?")))
    jogador["gols"] = golos[:]
    tot += golos[i]
    jogador["total"] = tot
print(jogador)
print("«»"*25)
for ky, val in jogador.items():
    print(f"O campo {ky} tem o valor {val}. ")
print(f'O jogador {jogador["nome"]}, jogou {partidas} partidas!')
print("«»"*25)
for x in range(0, partidas):
    print(f"    «=» Na partida {x}, fez {golos[x]} gols.")
print(f"Foi um total de {tot} gols.")
if tot > 3:
    print(" *** Brutal, que jogador da horaaaa!!    ***")
else:
    print("Ele podia fazer mais :(")
