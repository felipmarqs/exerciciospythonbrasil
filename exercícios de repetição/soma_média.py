#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
média = 0
cont = 0
for c in range(1,6):
    num = int(input("Digite um número: "))
    soma += num
média = soma/5
print(f"A soma dos 5 números é {soma} e a média é {média}.")