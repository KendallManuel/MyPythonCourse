n1 = int(input("Digite a primeira recta: "))
n2 = int(input("Digite a segunda recta: "))
n3 = int(input("Digite a terceira recta: "))
print("«»"*75)

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("Formam um triangulo")

    if n1 == n2 and n2 == n3:
        print("O triangulo é Equilátero")
    elif n1 == n2 and n1 < n3 or n1 > n3:
        print("O triangulo é Isósceles")
    elif n1 != n2 and n3:
        print("O triangulo é Escaleno")
else:
    print("Não formam um triangulo")