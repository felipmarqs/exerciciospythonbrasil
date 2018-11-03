#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime
d = int(input("Informe o dia:"))
m = int(input("Informe o mês: "))
a = int(input("Informe o ano: "))
if d > 31 or d < 0:
    print("Valor do dia inválido!")
if m > 12 or m < 0:
    print("Valor do mês inválido!")
if a > datetime.today().year or a < 1500:
    print("Valor do ano inválido!")
else:
    print(f"{d}/{m}/{a}")
