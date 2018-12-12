#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
continuar = 's'
cont = 0
while True:
    lista.append(int(input(f"Digite um número na posição {cont}: ")))
    continuar = str(input("Deseja continuar? [S/N]")).lower().strip()
    if continuar == 'n':
        break
    while continuar not in 'sn':
        print("Repete.")
        continuar = str(input("Deseja continuar? [S/N]")).lower().strip()
    cont += 1
print(f"Você digitou os valores {lista}")