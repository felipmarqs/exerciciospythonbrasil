'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

shrs = float(input("Quanto você ganha por hora ? R$"))
hrs = int(input("Quantas horas vocês trabalha por mês ? "))
salariob = shrs * hrs
ir = salariob * 0.11
inss = salariob * 0.08
sind = salariob * 0.05
salariol = salariob - (ir+inss+sind)

print(f"Salário bruto R${salariob:.2f}")
print(f"IR R${ir:.2f}")
print(f"INSS R${inss:.2f}")
print(f"Sindicato R${sind:.2f}")
print(f"Salário líquido R${salariol:.2f}")