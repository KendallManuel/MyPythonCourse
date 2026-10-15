num = int(input("Digite um número: "))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[31m", end=" ")
        total += 1
    else:
        print("\033[35m", end=" ")
    print("{}".format(i), end=" ")
print("\n\033[mO número {}, foi divisível {} vezes".format(num, total))
if total == 2:
    print("É por isso que ele é primo.")
else:
    print("É por isso ele não é primo.")
