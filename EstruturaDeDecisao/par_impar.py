#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
num = int(input("Digite um número para saber se é par ou ímpar: "))
if num % 2 == 0:
    print("É par!")
else:
    print("É impar!")