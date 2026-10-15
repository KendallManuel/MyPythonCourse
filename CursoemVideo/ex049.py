print("{:-^25}".format("TABUADA"))
n = int(input("Digite um nr:"))
c = 0
s = 0
for i in range(1, 11):
    c += 1
    s = n * c
    print("{:2} x {:2} = {:2}".format(n, c, s))
print("{:.^25}".format("FIM"))
