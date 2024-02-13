lista  = []
contP = 0

while True:
    pessoas = []
    nome = input("Qual o primeiro nome: ")
    contP += 1
    pessoas.append(nome)
    peso = int(input("Qual o peso: "))
    pessoas.append(peso)
    lista.append(pessoas[:]) #por enquanto eu só peguei os dados e copiei para uma lista 
    
    decisao  = input("Voçê quer continuar adicionando pessoas? ").upper().strip()
    if decisao in "N":
        break
#Agora eu quero pegar os valores das pessoas mais pesadas e leves    
pesoMenor = pesoMaior = 0
nomeMenor = [] #Nome das pessoas que pesam meno kilos
nomeMaior = []
contador = 0
while contador < len(lista):
    if contador == 0:
        pesoMaior = lista[contador][1]
        pesoMenor = lista[contador][1]
        nomeMenor = [lista[contador][0]]
        nomeMaior = [lista[contador][0]]
    else:
        if pesoMenor > lista[contador][1]:
            pesoMenor = lista[contador][1]
            nomeMenor = [lista[contador][0]]
        elif pesoMenor == lista[contador][1]:
            nomeMenor.append(lista[contador][0])
        
        if pesoMaior < lista[contador][1]:
            pesoMaior = lista[contador][1]
            nomeMaior = [lista[contador][0]]
        elif pesoMaior == lista[contador][1]:
            nomeMaior.append(lista[contador][0])
    contador += 1
        
print(f"A lista teve {contP} cadastradas, além disso essas foram as pessoas mais pesadas {nomeMaior}")
print(f"E essas foram com o menor peso {nomeMenor}")            
        
    
    



    