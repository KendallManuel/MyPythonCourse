def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2, 4, 6)
soma(1, 3)
soma(9, 4)