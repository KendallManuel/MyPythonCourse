pessoas = homens = mulheres = 0
masc = "M"
femn = "F"
while True:
    print("{:-^25}".format("CADASTRE UMA PESSOA"))
    idade = int(input("Idade: "))
    sexo = " "
    opção = " "
    while sexo not in "MmFf":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if sexo in "MmFf":
        print("-="*20)
        while opção not in "SsNn":
            opção = str(input("Você quer continuar? [S/N]"))
            #print("-=" * 20)
            if opção in "Ss":
                if idade > 18:
                    pessoas += 1
                if sexo in "Mm":
                    homens += 1
                if sexo == femn and idade < 20:
                    mulheres += 1
        if opção in "Nn":
            if idade > 18:
                pessoas += 1
            if sexo in "Mm":
                homens += 1
            if sexo == femn and idade < 20:
                mulheres += 1
            break
print("{:-^40}".format("FIM DE PROGRAMA!"))
print("Total de pessoas com mais de 18 anos de idade: {}".format(pessoas))
print("No total temos {} homens cadastrados".format(homens))
print("E temos {} mulheres com menos de 20 anos".format(mulheres))
