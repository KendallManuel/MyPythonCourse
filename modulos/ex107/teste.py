import moeda

valor = float(input('Digite o preco:  R$'))
print(f'A metade de {valor} e {moeda.metade(valor)}')
print(f'O dobro de {valor} e {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13)}')