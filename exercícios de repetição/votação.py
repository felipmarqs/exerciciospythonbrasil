#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
eleitores = int(input("Qual o número de eleitores ? "))
cont = 0
candidatoA = 0
candidatoB = 0
for e in range(0,eleitores):
    print("Candidato A = '1' B = '2' ")
    voto = int(input("Deseja votar em quem ? [1/2]: "))
    if voto == 1:
        candidatoA += 1
    elif voto == 2:
        candidatoB += 1
    else:
        print("Nulo!")
print(f"O candidato A recebeu {candidatoA} votos!")
print(f"O candidato B recebeu {candidatoB} votos!")