name = str(input('digite o nome:'))
if name == 'Alvaro':
    print("Bom nome")
elif name == 'Manuel, John, Rownan':
    print("Nome biblico")
elif name in "Carlos, Magda, Nick, Melanie, Tamy, Shenila, Mason, Warren, Ashley":
    print("O MEU FAMILIAR TEM O MESMO NOME!")
else:
    print("Que nome sem sal.")
print("Welcome, {}!". format(name))
