via = int(input("Qual é a distância da viagem? "))

if via <= 200:
    print(" O preço da viagem é de {}Mts". format(via*0.50))
else:
    print(" O preço da viagem é de {}Mts". format(0.45*via))


#0.50R/km (200km)
#0.45R/km (mais longas)