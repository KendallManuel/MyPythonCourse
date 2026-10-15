from random import randint
vitoria = 0
while True:
    user = int(input("Diga um valor: "))
    cpu = randint(0, 10)
    s = user + cpu
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar [P/I]? ")).strip().upper()[0]
    print("Você jogou {}, e o computador jogou {}. Total de {} ".format(user, cpu, s), end="")
    print("DEU PAR" if s % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if s % 2 == 0:
            print("VOCÊ VENCEU.")
            vitoria += 1
        else:
            print("VOCÊ PERDEU!")
            break
    elif tipo == "I":
        if s % 2 == 1:
            print("VOCÊ VENCEU.")
            vitoria += 1
        else:
            print("VOCÊ PERDEU!")
            break
    print("VAMOS JOGAR NOVAMENTE...")
print(f"GAME OVER! VOCÊ VENCEU {vitoria} VEZES")
