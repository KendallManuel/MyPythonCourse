frase = str(input("Digite algo: ")). upper().strip()
print("Quantas vezes aparece a letra A? ", frase.count("A"))
print("A letra aparece a primeria vez na posição nr: ", frase.find("A")+1)
print("A letra aparece a ultima vez na posição nr: ", frase.rfind("A")+1)
