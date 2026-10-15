l = float(input("Digite a largura da parede em metros:"))
h = float(input("Digite a altura da parede em metros:"))
a = float(l * h)
q = float(a / 2)
print("A área da parede é de: {:.1f}m2\n"
      "A quantidade de tinta necessária é de: {:.1f}l".format(a, q))
