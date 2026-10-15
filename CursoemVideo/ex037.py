num = int(input("Digite um número inteiro: "))
print("""Escolha uma base de conversão: 
[1] - Base Binária
[2] - Base Octal
[3] - Base Hexadecimal""")
opção = int(input("Digite a sua opção: "))
if opção == 1:
    print("{} na base binária é {} ".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} na base octal é {} ". format(num, oct(num)[2:]))
elif opção == 3:
    print("{} na base hexadecimal é {} ". format(num, hex(num)[2:]))
else:
    print("Opção Inválida!")
