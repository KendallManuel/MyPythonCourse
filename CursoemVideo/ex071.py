valor = int(input(" Quanto você quer levantar?$ "))
total = valor
notas = 50
totalnotas = 0
while True:
    if total >= notas:
        total -= notas
        totalnotas += 1

    else:
        if totalnotas > 0:
            print(f"Total de {totalnotas} notas de ${notas}")
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalnotas = 0
        if total == 0:
            break
print("-*"*20)
print("VOLTE SEMPRE AO BANCO KWAM!")
