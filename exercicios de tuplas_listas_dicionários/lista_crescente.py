#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
lista = list()
continuar = 's'
while continuar[0] in 's':
    valor = lista.append(int(input("Digite um valor: ")))
    if valor in lista:
        print("Valor duplicado!Não vou adicionar.")
        continuar = str(input("Quer continuar? [S/N] ")).lower().strip()
    continuar = str(input("Quer continuar? [S/N] ")).lower().strip()
print(f"Você digitou os valores {sorted(lista)}. ")
