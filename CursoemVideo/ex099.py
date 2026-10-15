valores = []
def maior(*num):
    while True:
        valores.append(int(input('Digite qualquer numero: ')))
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'Nn':
            break

maior(valores)
print(f'O maior valor inserido entre {valores} é {max(valores)}.')
