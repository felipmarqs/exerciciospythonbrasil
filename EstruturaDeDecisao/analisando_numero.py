'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.''' #wtf

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2

o = int(input("Qual operação deseja realizar? \n [1] SOMA \n [2] SUBTRAÇÃO \n [3] MULTIPLICAÇÃO \n [4]DIVISÃO:"))
if o == 1:
    print(f"A soma entre {n1} e {n2} é {s}!")
    if s > 0:
        print(f"{s} é positivo.")
    else:
        print(f"{s} é negativo")
    if s % 2 == 0:
        print(f"{s} é par.")
    else:
        print(f"{s} é ímpar.")
elif o == 2:
    print(f"A subtração entre {n1} e {n2} é {su}!")
    if su > 0:
        print(f"{su} é positivo.")
    else:
        print(f"{su} é negativo")
    if su % 2 == 0:
        print(f"{su} é par.")
    else:
        print(f"{su} é ímpar.")
elif o == 3:
    print(f"A multiplicação entre {n1} e {n2} é {m}!")
    if m > 0:
        print(f"{m} é positivo.")
    else:
        print(f"{m} é negativo")
    if m % 2 == 0:
        print(f"{m} é par.")
    else:
        print(f"{m} é ímpar.")
elif o == 4:
    print(f"A divisão de {n1} por {n2} é {d}")
    if d > 0:
        print(f"{d} é positivo.")
    else:
        print(f"{d} é negativo")
    if d % 2 == 0:
        print(f"{d} é par.")
    else:
        print(f"{d} é ímpar.")
else:
    print("Erro!")