try:
    a = int(input('Digite o numerador: '))
    b = int(input('Agora o denominador: '))
    result = a/b
except ValueError:
    print('Voce digitou um numero invalido!')
except ZeroDivisionError:
    print('Nao pode dividir qualquer valor por zero.')
except KeyboardInterrupt:
    print('\nO usuario nao digitou nenhum valor no teclado.')
except Exception as bug:
    print(f'O erro encontrado foi {bug.__context__}')
else:
    print(f'O resultado foi {result:.2f}')
finally:
    print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')