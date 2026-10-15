def notas(*num, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param num: Quantidade de notas dos alunos
    :param sit: Dispensado, Aprovado, Excluido
    :return: Dicionario com total de notas, maior nota, menor nota, media final e situacao (Opcional)
    """
    dicionario = {}
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num) / len(num)

    if sit:
        if dicionario['media'] > 14:
            dicionario['situacao'] = 'Dispensado'
        elif 14 > dicionario['media'] > 10:
            dicionario['situacao'] = 'Aprovado'
        else:
            dicionario['situacao'] = 'Excluido'
    return dicionario


# Programa Principal
resp = notas(15.5, 14.5, 19, 10)
print(resp)
print('-=' * 25)
help(notas)