from datetime import date
actual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = actual - nasc
print("Quem nasceu em  {}, tem {} anos em {}.".format(nasc, idade, actual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    print("Você está a {} anos de se alistar.".format(18-idade))
    print("Seu alistamento será em {}.".format(actual+(18-idade)))
elif idade > 18:
    print("Devia ter se alistado há {} anos.".format(idade-18))
    print("Seu alistamento será em {}.".format(actual-(18-idade)))
