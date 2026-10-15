pessoas = dict()
lista = list()
tot = totidade = 0
while True:
    pessoas["nome"] = str(input("Nome: ")).capitalize()
    while True:
        pessoas["sexo"] = str(input("Sexo: [M/F]")).strip().upper()[0]
        if pessoas["sexo"] in "MF":
            break
        else:
            print('Tente Novamente!')
    pessoas["idade"] = int(input("Idade: "))
    tot += 1
    totidade += pessoas["idade"]
    media = totidade/tot
    lista.append(pessoas.copy())
    while True:
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if opcao in "SN":
            break
    if opcao in "Nn":
        break
print("«»" * 25)
print(f"- O grupo tem ao todo {tot} pessoas.")
print(f"- A média de idade é de {media:.2f} anos.")
print('- As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista):
    if lista[i]["sexo"] in "Ff":
        print(f'{lista[i]["nome"]}', end=" ")
print()
print("- Lista das pessoas que estão acima da média: ")
for i, v in enumerate(lista):
    if lista[i]["idade"] > media:
        for key, value in v.items():
            print(f"{key} = {value}; ", end="")
        print()
        print()
print("«« ENCERRADO! »»")
