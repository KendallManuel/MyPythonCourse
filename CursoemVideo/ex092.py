from datetime import datetime
cidadao = {}
cidadao["nome"] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
cidadao["idade"] = datetime.now().year - ano
cidadao["ctps"] = int(input("Carteira de trabalho: [0 - não tem]"))
if cidadao["ctps"] != 0:
    cidadao["contracto"] = int(input("Ano de contractação: "))
    cidadao["salario"] = float(input("Salário: $"))
    cidadao["Aposentadoria"] = (cidadao["idade"] + ((cidadao["contracto"] + 35) - datetime.now().year))
print(cidadao)
for key, value in cidadao.items():
    print(f"    *{key} tem o valor {value}")
