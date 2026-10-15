frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

"""PARA ALÉM DO "CICLO FOR", PODEMOS USAR O COMANDO "INVERSO = JUNTO[::-1]" """

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("A frase {} é um palíndromo, porque invertida também é {}!".format(junto, inverso))
else:
    print("A frase {}, não é palíndromo, porque invertida ela é {}.".format(junto, inverso))
