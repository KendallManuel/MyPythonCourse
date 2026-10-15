num = [2, 5, 9, 1]
num[2] = 3
num.append(4)
num.sort(reverse=True)
num.insert(2, 7)
if 5 in num:
    num.remove(5)
else:
    print("SEM NÚMERO 5")
print(num)
print(f"A lista tem {len(num)} elementos")