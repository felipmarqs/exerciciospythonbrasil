'''Aprimore o desafio do aproveitamento dos jogadores para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador
time = list()
jogador = {'jogador':'','gols':[],'total': 0}
gols = list()
while True:
    jogador['jogador'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['jogador']} jogou? "))
    for p in range(0,partidas):
        gols.append(int(input(f"Quantos gols na partida {p}? ")))
    jogador['gols']= gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! REsponda apenas S ou N.")
    if resp == 'N':
        break
print("-" * 40)
print("cod",end = '')
for c in jogador.keys():
    print(f"{c:<15}",end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f"{k:>6} ",end='')
    for d in v.values():
        print(f"{str(d):<15}",end='')
    print()

'''
#incompleto