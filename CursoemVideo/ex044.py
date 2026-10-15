from time import sleep
print("{:=^50}".format("KWAM STORE"))
produto = float(input("Qual é o valor do produto?Mzn"))
print("«»"*75)
print("""Qual é a condição de pagamento? 
[1] - À vista dinheiro/cheque (10% de desconto)
[2] - À vista no cartão (5% de desconto) 
[3] - Em até 2x no cartão (preço normal)
[4] - 3x ou mais no cartão (20% de juros)""")

opção = int(input("Escolha a opção:"))
sleep(2)
print("Processado!")
if opção == 1:
    print("O valor a pagar é {:.2f} Mzn".format(produto-(produto*0.10)))
elif opção == 2:
    print("O valor a pagar é {:.2f} Mzn".format(produto-(produto*0.05)))
elif opção == 3:
    print("O valor a pagar é {:.2f} Mzn".format(produto))
elif opção == 4:
    print("O valor a pagar é {:.2f} Mzn".format(produto+(produto*0.20)))

else:
    print("Opção Inválida. Tente novamente!")
