ac = tot = 0
while True:
    num = int(input("Quer ver a tabuada de qual número? "))
    if num < 0:
        break
    while ac < 10:
        ac += 1
        tot = num * ac
        print("{:2} x {:2} = {:2}".format(num, ac, tot))
    print("=-"*10)
    ac = 0
print("FIM DE TABUADA. VOLTE SEMPRE!")
