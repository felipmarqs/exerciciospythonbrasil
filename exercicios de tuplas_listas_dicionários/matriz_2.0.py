#Aprimore o desafio de matriz anterior, mostrando no final: A soma de todos os valores pares digitados.. A soma dos valores da terceira coluna. O maior valor da segunda linha.
matriz = [],[],[]
matriz[0].append(int(input(f"Digite um valor para [0,0]: ")))
matriz[0].append(int(input(f"Digite um valor para [0,1]: ")))
matriz[0].append(int(input(f"DIgite um valor para [0,2]: ")))
matriz[1].append(int(input(f"Digite um valor para [1,0]: ")))
matriz[1].append(int(input(f"Digite um valor para [1,1]: ")))
matriz[1].append(int(input(f"Digite um valor para [1,2]: ")))
matriz[2].append(int(input(f"Digite um valor para [2,0]: ")))
matriz[2].append(int(input(f"Digite um valor para [2,1]: ")))
matriz[2].append(int(input(f"Digite um valor para [2,2]: ")))
print(f"[{matriz[0][0]}]",end=' ')
print(f"[{matriz[0][1]}]",end=' ')
print(f"[{matriz[0][2]}]",end=' ')
print(f"\n[{matriz[1][0]}]",end=' ')
print(f"[{matriz[1][1]}]",end=' ')
print(f"[{matriz[1][2]}]",end=' ')
print(f"\n[{matriz[2][0]}]",end=' ')
print(f"[{matriz[2][1]}]",end=' ')
print(f"[{matriz[2][2]}]",end=' ')
pares = 0
for c in range(0,3):
    for p in matriz[c]:
        if p % 2 == 0:
            pares += p
print(f"\n A soma de todos os números pares da matriz é {pares}")
soma3c = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"A soma de todos os números da terceira coluna é {soma3c}")
print(f"O valor mais alto da segunda linha é {max(matriz[1])}")