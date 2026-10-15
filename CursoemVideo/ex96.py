def area(l, c):
    dimensao = (l * c)
    print(f"A area de um terreno {l} x {c} é igual à {dimensao:.2f} metros.")


#Programa Principal
print('{:=^28}'.format("CONTROLE DE TERRENOS"))
area(l = float(input('Digite a largura do terreno: ')),
     c = float(input('Digite o comprimento do terreno: ')))
