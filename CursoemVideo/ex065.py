s = ac = maior = menor = m = 0
ajuda = 0
opção = ""
while opção in "Ss":
    num = int(input("Digite um número inteiro: "))
    opção = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    s += num
    ac += 1
    if ac == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
m = s / ac
print("Você digitou {} números e a média foi {:.2f}".format(ac, m))
print("O maior valor foi {} e o menor foi {} ".format(maior, menor))
