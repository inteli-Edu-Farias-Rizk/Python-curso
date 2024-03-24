dic = {}
dic['nome'] = input("Qual o nome: ")
dic['media'] = float(input("Qual a média do aluno: "))
if dic['media'] >= 6:
    dic['situacao'] = "Aprovado"
elif dic['media'] < 6:
    dic['situacao'] = 'Reprovado'
for k,v in dic.items():
    print(f"{k} é igual a {v}")