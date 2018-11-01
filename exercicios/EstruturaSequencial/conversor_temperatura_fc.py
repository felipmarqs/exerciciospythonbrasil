#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
f = int(input("Informe a temperatura em graus ºF:"))
c = (5 * (f - 32) / 9)
print(f"{f} graus Farenheit equivalem á {c:.2f} graus Celsius.")