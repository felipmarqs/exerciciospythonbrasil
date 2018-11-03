#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
print(f"O maior número é o {maior}.")