from random import randint
menor = maior = 0
print("Os valores sorteados foram: ", end="")
for contador in range(0, 5):
    tupla = randint(0, 10)
    print(tupla, end=" ")
    if contador == 0:
        maior = tupla
        menor = tupla
    elif tupla > maior:
        maior = tupla
    elif tupla < menor:
        menor = tupla
print(f"\nO maior valor foi: {maior} ")
print(f"O menor valor foi: {menor}")