#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = input("Digite um número para saber se é decimal ou inteiro: ")
if num.isdecimal() == True:
    print("É decimal!")
else:
    print("É real!")