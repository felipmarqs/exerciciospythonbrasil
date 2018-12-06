#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.
i = int(input("Digite o início: "))
f = int(input("Digite o fim: "))
soma = 0
for c in range(i,f+1):
    print(c)
    soma += c
print(f"A soma destes números é: {soma}",end='')