from datetime import date

#Funcao Para Eleicoes
def voto(n):
    """idade inferior a 18 --> Voto Negado
       idade entre: 18 e 65 --> Voto Obrigatorio
       idade acima de 65 --> Voto Opcional"""

    actual = date.today().year
    idade = actual - n
    global r1, r2, r3
    if idade < 18:
        r1 = idade
        return r1
    elif 18 <= idade <= 65:
        r2 = idade
        return r2
    else:
        r3 = idade
        return r3


#Programa Principal
print('-=' * 20)
ano = int(input('Em que ano voce nasceu: '))
r1 = r2 = r3 = voto(ano)
if r1 < 18:
    print(f'Com {r1} anos: VOTO PROIBIDO.')
elif 18 <= r2 <= 65:
    print(f'Com {r2} anos: VOTO OBRIGATORIO.')
else:
    print(f'Com {r3} anos: VOTO OPCIONAL.')
