num = s = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    s += num
#print("A SOMA DOS VALORES INSERIDOS FOI {}".format(s))
print(f"A soma entre os valores é {s}")