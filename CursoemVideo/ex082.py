num = []
par = []
impar = []
while True:
    valor = int(input("Digite um número: "))
    num.append(valor)
    resp = str(input("Quer continuar? [S/N]"))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    if resp in "Nn":
        break
print(f"A lista completa é: {num}")
print(f"A lista de pares é: {par}")
print(f"A lista de ímpares é: {impar}")
