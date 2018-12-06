#Faça um programa que leia 5 números e informe o maior número.
maior = 0
menor = 0
cont = 0
for c in range(1,6):
    num = int(input("Digite um número: "))
    if cont == 0:
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
print(f"O menor número é {menor}.")
print(f"O maior número é {maior}.")
