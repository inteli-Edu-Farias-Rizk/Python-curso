pares =[]
imp =[]
total = []
for c in range (0,7):
    num  = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        imp.append(num)
pares.sort()
imp.sort()
total.append(imp[:])
total.append(pares[:])
print(f"Os valores pares digitados foram{total[1]}")
print(f"Os valores impares digitados foram {total[0]}")