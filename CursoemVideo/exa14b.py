n = 1
heaven = odd = 0
while n != 0:
    n = int(input("Digite um numero: "))
    if n != 0:
        if n % 2 == 0:
            heaven += 1
        else:
            odd += 1
print("São {} nrs pares e {} nrs impares".format(heaven, odd))
