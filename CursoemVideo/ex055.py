pesomaior = 0
pesomenor = 0
for i in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(i)))
    if i == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print("O maior peso foi de {}kg".format(pesomaior))
print("O menor peso foi de {}kg".format(pesomenor))
