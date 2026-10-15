from datetime import date
actual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(i)))
    tot = actual - ano
    if tot >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Das 7 pessoas analisadas, {} são maiores de idade.".format(totmaior))
print("E {} são menores de idade.".format(totmenor))
