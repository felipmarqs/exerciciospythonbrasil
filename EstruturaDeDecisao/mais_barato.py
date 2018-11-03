#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input("Qual o preço do primeiro produto ? R$"))
p2 = float(input("Qual o preço do segundo produto ? R$"))
p3 = float(input("Qual o preço do terceiro produto ? R$"))
if p1 < p2 and p1 < p3:
    print("Compre o primeiro!")
elif p2 < p1 and p2 < p3:
    print(("Compre o segundo!"))
elif p3 < p1 and p3 < p2:
    print("Compre o terceiro!")
