#Funcao Para Eleicoes
def voto(ano):
    from datetime import date
    actual = date.today().year
    idade = actual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    elif 16 < idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


#Programa Principal
print('-=' * 20)
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
