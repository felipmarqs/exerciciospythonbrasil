'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''
salarioa = float(input("Qual seu salário? "))
salariob = salarioa
if salarioa <= 280:
    salariob += salarioa * 0.20
    print("Você recebeu um aumento de 20%")
elif salarioa > 280 and salarioa <= 700:
    salariob += salarioa *0.15
    print("Você recebeu um aumento de 15%")
elif salarioa > 270 and salarioa <= 1500:
    salariob += salarioa * 0.10
    print("Você recebeu um aumento de 10%")
elif salarioa > 1500:
    salariob += salarioa * 0.05
    print("Você recebeu um aumento de 5%")
print(f"Seu salário era R${salarioa}.")
print(f"Seu salário atual é R${salariob}.")
aumento = salariob - salarioa
print(f"O aumento foi de R${aumento}")