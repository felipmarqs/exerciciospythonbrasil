#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor na posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f"O maior valor foi {max(lista)} nas posições ",end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end='')
print(f"\nO menor valor foi {min(lista)} nas posições ",end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f"{i}...",end='')
