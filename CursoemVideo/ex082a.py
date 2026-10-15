num = list()
impar = list()
par = list()
while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
for pos, valor in enumerate(num):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
print("=-"*30)
print(f"A lista completa é {num}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")
