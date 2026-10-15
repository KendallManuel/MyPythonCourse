teste = list()
teste.append("Kendall")
teste.append(22)
pessoas = list()
pessoas.append(teste[:])
teste[0] = "Mary"
teste[1] = 19
pessoas.append(teste[:])
print(pessoas)
