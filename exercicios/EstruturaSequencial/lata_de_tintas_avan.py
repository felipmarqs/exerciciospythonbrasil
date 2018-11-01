from math import  ceil
'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''
a = float(input("Qual o tamanho em metros quadrados da área a ser pintada ?"))
l = (a * 1) / 6
print(f"{l:.2f} litros")
print(f"Para não faltar você precisa de {ceil(l)} litros")
print("Cada lata custa R$80 e tem 18 litros")
print("Cada galão custa R$25 e tem 3.6L")
latas = (ceil(l) * 1) / 18
galoes = (ceil(l) * 1) / 3.6
print(f"Se você comprar apenas latas de 18L precisará comprar {ceil(latas)} e custará R${ceil(latas) * 80} ")
print(f"Se você comprar apenas galões de 3.6 L precisará de {ceil(galoes):.2f} e custará R${ceil(galoes) * 25}")
#print(f"Se você quiser comprar galões e latas para deixar o preço mais acessível compre {latas} e {galoes}")
#não consegui fazer a terceira condição