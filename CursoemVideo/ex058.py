from random import randint
cpu = randint(0, 10)
print("«»"*77)
print("Olá! Sou o seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar?")
print("""1 - SIM
2 - NÃO""")
opção = int(input("Escolha uma opçaõ: "))
print("-"*25)
acertou = False
tentativas = 0
if opção == 1:
    while not acertou:
        user = int(input("Qual é o seu palpite? "))
        tentativas += 1
        if user == cpu:
            acertou = True
        else:
            if user < cpu:
                print("Dica: Está acima do número escolhido- Tente novamente:")
                print("-"*25)
            elif user > cpu:
                print("Dica: Está abaixo do número escolhido. Tente novamente: ")
                print("-"*25)
    print("Acertou com {} tentativas. Você está de parabéns!".format(tentativas))
elif opção == 2:
    print("Tudo bem! Até a próxima.")

else:
    print("Opção Inválida!")
