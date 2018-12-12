#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.
números = [[],[]]
pares = list()
impares = list()
for c in range(0,7):
    dado = int(input(f"Digite o {c+1}º número: "))
    if dado % 2 == 0:
        pares.append(dado)
    elif dado % 2 == 1:
        impares.append(dado)
números[0].append(pares)
números[1].append(impares)
print(f"Os números pares digitados foram: {números[0]}")
print(f"Os números impares digitados foram: {números[1]}")
