standings = ("Fc Barcelona", "Real Madrid", "Atletico Madrid",
             "Atletic Bilbao", "Villareal", "Real Betis",
             "Mallorca", "Celta Vigo", "Rayo Vallecano",
             "Sevilla", "Getafe", "Real Sociedade",
             "Girona", "Osasuna", "Espanyol",
             "Valencia", "Alaves", "CD Leganes",
             "Las Palmas", "Real Valladolid")
print("Os últimos classicados na tabela são: ")
for indice in range(-4, 0):
    print(f" *{standings[indice]}")
print("-"*30)
print(f"Equipes em ordem alfabética: {sorted(standings)}")
print("-"*30)
print(f'O Barcelona está na {standings.index("Fc Barcelona")+ 1}ª posição')
print("-"*30)
print("Os 5 primeiros na tabela são: ")
for posicao, equipe in enumerate(standings):
    if posicao < 5:
        print(f" {posicao +1}ª posição -> {equipe}")

