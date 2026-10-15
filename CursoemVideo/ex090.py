aluno = dict()
situacao = {"a": "Aprovado", "b": "Reprovado"}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))
print(f"Nome é igual a {aluno['Nome']}")
print(f"A média do {aluno['Nome']} é igual a {aluno['Média']} valores")
if aluno["Média"] >= 12:
    print(f'A situação é igual a {situacao["a"]}')
else:
    print(f"A situação é igual a {situacao['b']}")