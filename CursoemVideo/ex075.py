s1 = s2 = s3 = s4 = 0
par = 0
for cont in range(0, 4):
    num = int(input("Digite um número: "))
    if cont == 0:
        s1 = num
        if s1 % 2 == 0:
            par += 1
    if cont == 1:
        s2 = num
        if s2 % 2 == 0:
            par += 1
    if cont == 2:
        s3 = num
        if s3 % 2 == 0:
            par += 1
    if cont == 3:
        s4 = num
        if s4 % 2 == 0:
            par += 1
    tupla = (s1, s2, s3, s4)
print(f"Foram digitados os números: {tupla}")
print(f"O número 9 aparece {tupla.count(9)} vezes.")
if s1 == 3:
    print(f"O número 3 apareceu na {tupla.index(3)+ 1}ª posição.")
elif s2 == 3:
    print(f"O número 3 apareceu na {tupla.index(3)+ 1}ª posição.")
elif s3 == 3:
    print(f"O número 3 apareceu na {tupla.index(3)+ 1}ª posição.")
elif s4 == 3:
    print(f"O número 3 apareceu na {tupla.index(3)+ 1}ª posição.")
else:
    print("O número 3 não apareceu em nenhuma posição.")
print(f"Foram {par} números pares digitados.")