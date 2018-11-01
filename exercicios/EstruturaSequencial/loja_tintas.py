#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
a = float(input("Quantos metros quadrados é a área que deseja pintar ? "))
l = (a * 1) / 3
print(f"Para pintar {a} m² você precisa de {l:.2f} litros de tinta ")
print(f"Cada lata de 18 litros custa R$ 80.")
latas = (l/18)
print(f"Você terá que comprar { math.ceil(latas)} latas e isso vai custar R${math.ceil(latas)*80}.")