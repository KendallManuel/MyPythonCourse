from datetime import date
ano = int(input("Digite o ano do seu nascimento:"))
actual = date.today().year
idade = actual - ano

if idade < 9:
    print("Você tem {} anos. A sua categoria é: MIRIM". format(idade))
elif idade <= 14:
    print("Você tem {} anos. A sua categoria é: INFANTIL".format(idade))
elif idade <= 19:
    print("Você tem {} anos. A sua categoria é: JUNIOR".format(idade))
elif idade <= 20:
    print("Você tem {} anos. A sua categoria é: SÊNIOR".format(idade))
else:
    print("Você tem {} anos. A sua categoria é: Master".format(idade))
