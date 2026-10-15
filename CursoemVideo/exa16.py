lanche = ("Burger", "Juice", "Pizza", "Ice cream", "Chips")

for indice in range(0, len(lanche)):
    print("Eu vou comer {}".format(lanche[indice]))
print("-"*30)

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("-" * 30)

for posicao, comida in enumerate(lanche):
    print(f"Eu vou comer {comida}, na {posicao+1}a posicao")

print("ESTOU EMPANTORRADO!")
