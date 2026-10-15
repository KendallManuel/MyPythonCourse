standings = ("Fc Barcelona", "Real Madrid", "Atletico Madrid",
             "Atletic Bilbao", "Villareal", "Real Betis",
             "Mallorca", "Celta Vigo", "Rayo Vallecano",
             "Sevilla", "Getafe", "Real Sociedade",
             "Girona", "Osasuna", "Espanyol",
             "Valencia", "Alaves", "CD Leganes",
             "Las Palmas", "Real Valladolid")
print("-"*30)
print(f"Tabela da LaLiga: {standings}")
print("-"*30)
print(f"As 5 primeiras classificadas são: {standings[0:5]}")
print("-"*30)
print(f"As 4 últimas classificadas são: {standings[-4:]}")
print("-"*30)
print(f"O Real Betis está na {standings.index('Real Betis')+ 1}ª posição da tabela")
