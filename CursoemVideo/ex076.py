produtos = ("bola", "4.5", "laptop", "300", "joy", "9", "iphone", "999", "car", "3650", "tv", "235", "partybox320", "350", "boombox3", "189")
par = 0
imp = 1
print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50, end="")
for indice in range(0, len(produtos), 2):
    print(f"\n{produtos[par]:.<50}", end="")
    print(f"${produtos[imp]:>4}", end=" ")
    par += 2
    imp += 2
print("\nFim da compra!".upper())
