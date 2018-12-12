#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. DEpois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário. Incluindo o total de gols feitos durante o campeonato
dados = {'jogador':'','gols':[],'total': 0}
gols = list()
dados['jogador'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {dados['jogador']} jogou? "))
for p in range(0,partidas):
    gols.append(int(input(f"Quantos gols na partida {p}? ")))
dados['gols']= gols[:]
dados['total'] = sum(gols)
print("-="*20)
print(dados)
print("-="*20)
for k,v in dados.items():
    print(f"O campo {k} tem o valor {v}.")
print("-="*20)
print(f"O jogador {dados['jogador']} jogou {partidas} partidas")
for i,v in enumerate(dados['gols']):
    print(f"=> Na partida {i}, fez {v} gols.")
print(f"Foi um total de {dados['total']} gols.")