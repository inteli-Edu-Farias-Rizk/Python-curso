todos = []

while True:
    dic = {}
    dic["gols"] = []
    dic["nome"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {dic['nome']} jogou: "))

    for c in range(partidas):
        num = int(input(f"Quantos gols na partida {c+1}? "))
        dic["gols"].append(num)
    
    dic['total'] = sum(dic['gols'])
    todos.append(dic)
    
    resposta = input("Você gostaria de continuar? (S/N): ")
    if resposta.lower() == "n":
        break

print("\n" + "-"*45)
print(f"{'Nome':<15}{'Gols por Partida':<20}{'Total de Gols'}")
print("-"*45)

for jogador in todos:
    print(f"{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total']}")

escolha = input("Mostrar os dados de qual jogador? ")
for jogador in todos:
    if jogador['nome'] == escolha:
        print("\n" + "-"*45)
        print(f"Dados do jogador {escolha}:")
        print(f"{'Partida':<10}{'Gols':<10}")
        print("-"*45)
        for partida, gols in enumerate(jogador['gols'], start=1):
            print(f"{partida:<10}{gols:<10}")
        print("-"*45)
        print(f"Total de gols: {jogador['total']}")
        break
else:
    print(f"Jogador {escolha} não encontrado.")
