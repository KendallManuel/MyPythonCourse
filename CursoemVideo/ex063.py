print("{:-^50}".format("SEQUÊNCIA DE FIBONACCI!"))
num = int(input("Quantos termos da série de fibonacci você que mostrar? "))
primeirotermo = 0
segundotermo = 1
print("{} -> {}".format(primeirotermo, segundotermo), end="")
ac = 3
while ac <= num:
    terceirotermo = primeirotermo + segundotermo
    print(" -> {}".format(terceirotermo), end="")
    primeirotermo = segundotermo
    segundotermo = terceirotermo
    ac += 1
print(" -> Fim!", end="")
