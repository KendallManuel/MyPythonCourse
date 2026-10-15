extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezasseis", "dezassete", "dezoito", "dezanove", "vinte")
algarismo = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
num = int(input("Digite um número entre 0 e 20: "))
if 0 <= num <= 20:
    print("Você escolheu o número {}.".format(extenso[num]))
else:
    while num not in algarismo:
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você escolheu o número {extenso[num]}.")
    print("-"*50)
    print("Fim de programa. Volte sempre!!!")
