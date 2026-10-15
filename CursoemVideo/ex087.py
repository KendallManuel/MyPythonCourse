matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = soma = pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        #Soma dos pares da matriz
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        #Soma dos valores da terceira coluna
        soma += matriz[l][2]
        #Maior valor da segunda linha
        if matriz[1][c] == 0:
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
#Exibição na tela
print("«»"*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
print("«»"*20)
print(f"A soma dos valores pares é de [{pares:^1}]")
print(f"A soma dos valores da terceira coluna é de [{soma:^1}]")
print(f"O maior valor da segunda linha é [{maior:^1}]")