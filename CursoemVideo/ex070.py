total = n = barato = ac = 0
nome = " "
cancelar = False
print("*" * 40)
print("{:.^40}".format("SUPERMERCADO KWAM"))
print("*" * 40)
while not cancelar:
    produto = str(input("Nome do Produto? "))
    preço = float(input("Preço?$"))
    total += preço
    ac += 1
    if preço > 1000:
        n += 1
    if ac == 1:
        barato = preço
        nome = produto
    else:
        if preço < barato:
            nome = produto
            barato = preço
    opção = " "
    while opção not in ("SsNn"):
        opção = str(input("Vai querer adicionar mais itens ao carinho? [S/N]")).strip().upper()[0]
    if opção in "Nn":
        cancelar = True
print("-=" * 20)
print(f"O total da compra foi {total}")
print(f"Temos {n} produtos custando mais de $1000.00")
print(f"O produto mais barato foi {nome} que custa ${barato}")