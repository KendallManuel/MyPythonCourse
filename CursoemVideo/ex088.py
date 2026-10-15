from random import randint
from time import sleep
print("«»"*15)
print("{:=^30}".format("JOGA NA MEGA SENA"))
print("«»"*15)
rounds = []
num = int(input("Quanto jogos você quer que eu sorteie? "))
rounds.append(num)
print("{:^30}".format(f"...Sorteando {num} jogos..."))
print("«»"*15, end="")
for n in range(0, num):
    sleep(1)
    for cada in rounds:
        print()
        print(f"jogo {n+1}: ", end="[")
        for i in range(1, 7):
            cpu = randint(1, 60)
            print(f"{cpu}", end=" ")
        print("]", end="")
print()
sleep(1)
print("{:-^30}".format("BOA SORTE!"))
