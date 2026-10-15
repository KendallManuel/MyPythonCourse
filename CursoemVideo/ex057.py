sexo = str(input("Escolha o sexo da pessoa [M/F]: ")).strip()[0]
#c = 1
masc = "M" and "m"
femn = "F" and "f"
genero = ""
if sexo in "Mm":
    print("Sexo masculino escolhido com sucesso.")
elif sexo in "Ff":
    print("Sexo femenino escolhido com sucesso.")
else:
    while genero != masc and genero != femn:
        print("Tente novamente!")
        print("«»"*20)
        genero = str(input("Escolha o sexo da pessoa novamente: ")).strip()[0]
        if genero == masc:
            print("Sexo masculino escolhido com sucesso.")
        if genero == femn:
            print("Sexo feminino escolhido com sucesso.")

    print("{:-^50}".format("Obrigado!"))
