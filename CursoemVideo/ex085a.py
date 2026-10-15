valores = [[], []]
num = 0
for i in range(1, 8):
    num = int(input(f"Digite o {i}º. valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print("«»"*30)
print(f"Os valores pares digitados foram: {valores[0]}")
print(f"Os valores ímpares digitados foram: {valores[1]}")
