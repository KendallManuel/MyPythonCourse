ac = 0
maisvelho = 0
name = ""
mulheresmenores = 0
for k in range(1, 5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(k))).strip()
    idade = int(input("Digite a idade da {}ª pessoa: ".format(k)))
    sexo = str(input("Escolha o sexo da {}ª pessoa (M/F): ".format(k))).strip()
    ac += idade
    if k == 1 and sexo in "Mm":
        maisvelho = idade
        name = nome
        if sexo in "Ff" and idade < 20:
            mulheresmenores = 1
    else:
        if sexo in "Mm" and idade >= maisvelho:
            maisvelho = idade
            name = nome
        if sexo in "Ff" and idade < 20:
            mulheresmenores += 1
    print("«»"*20)
print("A média das idades do grupo é {}".format(ac/4))
print("O nome do homem mais velho do grupo é {}, com {} anos de idade".format(name, maisvelho))
print("Existem {} mulheres com menos de 20 anos.".format(mulheresmenores))
