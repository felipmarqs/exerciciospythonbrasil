#Faça um Programa que leia três números e mostre-os em ordem decrescente
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2 > n3:
    print(n1,n2,n3)
elif n1 > n3 > n2:
    print(n1,n3,n2)
elif n2 > n1 > n3:
    print(n2,n1,n3)
elif n2 > n3 > n1:
    print(n2,n3,n1)
elif n3 > n1 > n2:
    print(n3,n1,n2)
elif n3 > n2 > n1:
    print(n3,n2,n1)
else:
    print('erro')