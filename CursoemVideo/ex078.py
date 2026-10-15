maior = menor =0
numeros = list()
for i in range(0, 5):
    numeros.append(int(input(f"Digite um número para a {i+1}ª posição : ")))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print("="*40)
print(f"Você digitou os números: {numeros}")
print(f"O maior número digitado foi {maior}, nas posições", end=" ")
for pos, val in enumerate(numeros):
    if val == maior:
        print(f"{pos+1}...", end=" ")
print()
print(f"O menor número digitado foi {menor}, nas posições", end=" ")
for pos, val in enumerate(numeros):
    if val == menor:
        print(f"{pos+1}...", end="")
