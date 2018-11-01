#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
dph = float(input("Quanto você ganha por hora ?"))
horas = int(input("Quantas horas vocês trabalha por mês?"))
salario = dph * horas
print(f"Você trabalha {horas} e ganha R${dph} por hora, no final do mês seu salário será de R${salario}.")