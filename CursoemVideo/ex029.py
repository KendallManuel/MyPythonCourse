speed = int(input("Digite a velocidade do carro: "))
if speed >= 80:
    print(" EXCESSO DE VELOCIDADE!!! \n Você será multado! A multa vai custar {:.0f}mts". format((speed-80)*7))
else:
    print("Tenha uma boa viagem!")
