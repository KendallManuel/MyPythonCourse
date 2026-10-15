valores = []
par = list()
impar = []
for i in range(0, 7):
    valores.append(int(input(f"Digite o {i+1}º. valor: ")))
    if valores[i] % 2 == 0:
        par.append(valores[i])
    else:
        impar.append(valores[i])
par.sort()
impar.sort()
print(f"Os valores pares digitados foram: {par}")
print(f"Os valores ímpares digitados foram: {impar}")
