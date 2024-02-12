matriz = [[],
          [],
          []
          ]
count = 0
while count < 3:
    for c in range(0,3):
        num = int(input(f"DIgite um valor para [{count},{c}]: "))
        matriz[count].append(num)
    count += 1
print(matriz)
print("++"*30)
for p in matriz[0]:
    print(f"[{p:^5}]" ,end="")
print()
for x in matriz[1]:
    print(f"[{x:^5}]", end="")
print()
for t in matriz[2]:
    print(f"[{t:^5}]", end ="")