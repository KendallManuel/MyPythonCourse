tot = s = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 999:
        break
    tot += 1
    s += num
print("Você digitou {} números e a soma entre eles foi {}".format(tot, s))
