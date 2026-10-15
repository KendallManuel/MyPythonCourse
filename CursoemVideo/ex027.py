name = str(input("Insira o seu nome: ")).strip()
primeiro = name.split()
print("O seu primeiro nome é: ", primeiro[0])
print("O seu último nome é: ", primeiro[len(primeiro)-1])
