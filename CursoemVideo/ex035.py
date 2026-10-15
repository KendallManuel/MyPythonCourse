n1 = int(input("Digite a primeira recta: "))
n2 = int(input("Digite a segunda recta: "))
n3 = int(input("Digite a terceira recta: "))
print("«»"*25)
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("Formam um triangulo")
else:
    print("Não formam um triangulo")
    