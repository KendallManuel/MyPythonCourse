from random import randint
from time import sleep
print("ESCOLHENDO UM NUMERO...")
sleep(2)
print("ESCOLHIDO!")
cpu = randint(0, 5)
user = int(input("Adivinhe o numero: "))
if user == cpu:
    print("Você acertou! O numero escolhido pelo computador foi {}". format(cpu))
else:
    print("Você errou! O numero escolhido pelo computador foi {}". format(cpu))
