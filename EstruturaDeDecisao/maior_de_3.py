#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
print(f"O maior número foi {maior}")