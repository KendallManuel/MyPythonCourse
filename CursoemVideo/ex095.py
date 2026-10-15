jogador = {}
golos = []
dados = list()
while True:
    tot = 0
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    golos.clear()
    for i in range(0, partidas):
        golos.append(int(input(f"Quantos golos na partida {i}?")))
        jogador["gols"] = golos[:]
        tot += golos[i]
        jogador["total"] = tot
    dados.append(jogador.copy())
    while True:
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if opcao in "SN":
            break
        print("ERRO! Responde apenas S ou N.")
    if opcao in "Nn":
        break
print("«»" * 30)
print("cod", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 40)
for k, v in enumerate(dados):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 - interrompe!)"))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f"ERRO! Não existe jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {dados[busca]['nome']}")
        for i, g in enumerate(dados[busca]["gols"]):
            print(f"    No jogo {i+1} fez {g} gols")
    print("-" * 40)
print("«« VOLTE SEMPRE »»")
print(dados)
print(jogador['gols'][1])
