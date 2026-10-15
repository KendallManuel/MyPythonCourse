palavras = ("Andar", "Almocar", "Aprender", "Banir", "Bagunca", "Banana", "Casa", "Cebola", "Constipado", "Dancar", "Debilitado", "Dominio", "Entediado", "Etanol", "Envio", "Fadiga")
for indice, pal in enumerate(palavras):
    print(f"\nNa palavra *{pal.upper()}*, temos as seguintes vogais -> ", end=" ")
    for letra in pal:
        if letra.lower() in "aeiou":
            print(f"{letra.lower()}", end=" ")
