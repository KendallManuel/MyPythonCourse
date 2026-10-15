from random import randint
from time import sleep
print('{:=^75}'.format("JokenPO"))
print("Gostaria de jogar JokenPO comigo?")
print("""[1] - SIM
[2] - NÃO""")
print("-"*75)
opção = int(input("Escolha a opção:"))
print("-"*75)
itens = ("Pedra", "Papel", "Tesoura")
cpu = randint(0, 2)
if opção == 1:
    print("""[0] - Pedra
[1] - Papel
[2] - Tesoura""")
    print("-"*75)
    user = int(input("Faça a sua escolha:"))
    print("-"*75)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    print("-"*75)
    print("Computador escolheu {}".format(itens[cpu]))
    print("Você escolheu {}".format(itens[user]))
    print("-"*30)
    if cpu == 0:
        if user == 0:
            print("EMPATE:|")
        elif user == 1:
            print("VOCÊ VENCEU:)")
        elif user == 2:
            print("VOCÊ PERDEU:(")
        else:
            print("JOGADA INVÁLIDA!")
    elif cpu == 1:
        if user == 0:
            print("VOCÊ PERDEU:(")
        elif user == 1:
            print("EMPATE:|")
        elif user == 2:
            print("VOCÊ VENCEU:)")
        else:
            print("JOGADA INVÁLIDA!")
    elif cpu == 2:
        if user == 0:
            print("VOCÊ VENCEU:)")
        elif user == 1:
            print("VOCÊ PERDEU:(")
        elif user == 2:
            print("EMPATE:|")
        else:
            print("JOGADA INVÁLIDA!")
    else:
        print("Opção inválida!")

elif opção == 2:
    print("Que pena! Amaria ganhar de você. kkk")
else:
    print("Opção Inválida. Tente novamente...")
print("«»"*50)