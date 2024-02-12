lista = []
for c in range (1,6):
    valor = int(input("Digite um novo valor: "))
    if c == 1 or valor > lista[-1]:
        lista.append(valor)
    else:
        x = 0
        while x < len(lista):
            if valor < lista[x]:
                lista.insert(x,valor)
                break
            x =+ 1
print(lista)





    