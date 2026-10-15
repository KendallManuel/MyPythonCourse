cancelar = False
while not cancelar:
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    s = num1 + num2
    m = num1 * num2
    igual = 0
    maior = 0
    print("""[1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa""")
    opção = int(input("Esolha uma opção: "))
    if opção == 1:
        print("A soma de {} + {} = {}".format(num1, num2, s))
        #exit()
    if opção == 2:
        print("A multiplicação de {} x {} = {}".format(num1, num2, m))
        #exit()
    if opção == 3:
        if num1 > num2:
            maior = num1
            print("O maior valor é {}".format(maior))
        elif num1 == num2:
            print(f"Os valores são iguais. {num1} e {num2}")
        elif num2 > num1:
            maior = num2
            print("O maior valor é {}".format(maior))
        #exit()
    if opção == 4:
        print("")

    if opção == 5:
        cancelar = True
        exit("FIM! Obrigado!")
