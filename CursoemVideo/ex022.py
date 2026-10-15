name = str(input("Escreva o seu nome completo: ")). strip()
print("\n O nome com todas maiúsculas:", name.upper(),
      "\n O nome com todas minusculas:", name.lower(),
      "\n Total de letras sem espaços:", len(name) - name.count(" "))
primeiro = name.split()
print(" O primeiro nome tem:", len(primeiro[0]), "letras")
