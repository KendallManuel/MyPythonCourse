palavras = ("Andar", "Almocar", "Aprender", "Banir", "Bagunca", "Banana", "Casa", "Cebola", "Constipado", "Dancar", "Debilitado", "Dominio", "Entediado", "Etanol", "Envio", "Fadiga")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
