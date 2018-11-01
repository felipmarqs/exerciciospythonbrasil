'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo'''
n1= int(input("Digite um número inteiro:"))
n2= int(input("Digite outro número inteiro:"))
n3 = float(input("Digite um número real:"))

r1 = (n1 * 2) * (n2 / 2)
r2 = (3*n1) + n3
r3 = n3**3

print(f"O produto do dobro do primeiro com metade do segundo é {r1}")
print(f"A soma do triplo do primeiro com o terceiro é {r2}.")
print(f"o terceiro elevado ao cubo é {r3}")