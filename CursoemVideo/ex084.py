pessoas = list()
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp in "Nn":
        break
print("«»"*30)
print(f"No total foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")
for cadapessoa in pessoas:
    if cadapessoa[1] == maior:
        print(f"[{cadapessoa[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for cadapessoa in pessoas:
    if cadapessoa[1] == menor:
        print(f"[{cadapessoa[0]}] ", end="")
print()