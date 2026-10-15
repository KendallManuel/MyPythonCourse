num = list()
while True:
    valor = int(input("Digite um número: "))
    if valor not in num:
        num.append(valor)
        print("Número adicionado com sucesso...")
    else:
        print("Número duplicado. Tente outro!")
    resposta = str(input("Quer continuar? [S/N] "))
    if resposta in "Nn":
        break
print("-="*30)
num.sort()
print(f"Você digitou os números {num}")