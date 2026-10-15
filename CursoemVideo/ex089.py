alunos = []
dados = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Teste1: ")))
    dados.append(float(input("Teste2: ")))
    alunos.append(dados[:])
    dados.clear()
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp in "Nn":
        break
print("«»"*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print("-"*25)
for id, notas in enumerate(alunos):
    print(f"{id:<4}{alunos[id][0]:<10}{(notas[1]+notas[2])/2:>10.1f}")
print("-"*30)
while True:
    display = int(input("Quer ver nota de qual aluno? (Press 999 to cancel): "))
    for id, notas in enumerate(alunos):
        if display == id:
            print(f"Notas de {alunos[id][0]} são [{notas[1]} e {notas[2]}]")
    if display == 999:
            break
print("-"*50)
print("PROGRAMA ENCERRADO.")
print("««« VOLTE SEMPRE »»»")
