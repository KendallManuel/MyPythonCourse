tot = s = 0
cancelar = False
while not cancelar:
    num = int(input("[Escreva 999 para terminar] || Digite um número inteiro: "))
    if num != 999:
        s += num
        tot += 1
    else:
        cancelar = True
        print("Você digitou {}. Isso significa para mim -<>- FIM DE PROGRAMA!".format(999))
        print("{:.^55}".format("DESCONSIDERANDO O FLAG"))
print("Foram {} números digitados e a soma entre eles é {}".format(tot, s))
