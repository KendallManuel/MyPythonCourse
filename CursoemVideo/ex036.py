valor = float(input("Qual é o valor da casa que pretende adquirir?"))
salário = float(input("Qual é o valor do seu salário?"))
anos = int(input("Em quantos anos pretende pagar o casa?"))
total = valor/(anos*12)
mensal = total
print("«»"*100)
if mensal <= salário * 0.30:
    print("Para poder pagar uma casa de {}Mzn, em {} anos, a prestação será de {}Mzn/mês. \n Parabéns, você pode comprar à casa. :)".format(valor, anos, mensal))

else:
    print("Para poder pagar uma casa de {}Mzn, em {} anos, a prestação será de {}Mzn/mês. \n Oops, você não está condionado a pagar a casa! :(".format(valor, anos, mensal))

print("Atentamente!")
