print("{:-^50}".format("PROGRESSÃO ARITMÉTICA V2.0"))
primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão da progressão aritmética: "))
tot = (primeiro + razão)
c = 0
print("{} {}".format(primeiro, "->"), end=" ")
while c < 9:
    print("{} {}".format(tot, "->"), end=" ")
    c += 1
    tot += razão
print("Fim!", end="")

