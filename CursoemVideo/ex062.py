print("{:-^50}".format("SUPER PROGRESSÃO ARITMÉTICA V3.0"))
primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
tot = primeiro + razão
c = 0
k = 0
print("{} -> ".format(primeiro), end="")
while c < 9:
    print("{} -> ".format(tot), end="")
    c += 1
    tot += razão
print("PAUSA!")
maistermos = int(input("Quantos mais termos você quer? "))
if maistermos == 0:
        print("Fim!")
else:
    while k < maistermos:
        print("{} -> ".format(tot), end="")
        tot += razão
        k += 1
    print("Fim!")
