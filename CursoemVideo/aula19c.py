estado = dict()
moz = list()
for c in range(0, 3):
    estado["Província"] = str(input("Nome da província: "))
    estado["Sigla"] = str(input("Sigla: "))
    moz.append(estado.copy())
print(moz)
print(estado)
for est in moz:
    for valor in est.values():
        print(valor, end=" ")
    print()
