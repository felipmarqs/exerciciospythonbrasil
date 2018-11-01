#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
h = float(input("Qual sua altura ?"))
s = str(input("Você é homem ou mulher ? [H/M]?")).lower()
if s == 'h':
    pi=(72.7 * h) - 58
elif s == 'm':
    pi = (62.1*h) - 44.7
print(f"Seu peso ideal é {pi:.2f}.")