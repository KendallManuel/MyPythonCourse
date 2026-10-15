s = int(input("Qual é o seu salário?"))
quinze = s*0.15
dez = s*0.10

if s <= 1250:
    print("O seu salario é {}Mts, com um bonus de {}Mts. Totaliza {}Mts ".format(s, quinze, s+quinze))
else:
    print("O seu salario é {}Mts, com um bonus de {}Mts. Totaliza {}Mts ".format(s, dez, s+dez))
