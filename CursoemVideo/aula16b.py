valores = []
valores.append(5)
valores.append(9)
valores.append(4)
del valores[0]
valores.pop(1)
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("FIM DA LISTA")
