print("{:-^30}".format("DESAFIO 081"))
num = list()
while True:
    valor = int(input("Digite um número: "))
    num.append(valor)
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print("«»"*30)
print(f"Você digitou os números: {num}")
print(f"Que são um total de {len(num)} elementos.")
num.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {num}")
if 5 in num:
    print("O número 5 existe na lista.")
else:
    print("O número 5 não faz parte da lista.")
