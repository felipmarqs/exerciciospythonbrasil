#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
cds = int(input("Quantos CD's você tem? "))
cont = 0
media = 0
gasto = 0
while cont < cds:
    cont += 1
    valor = int(input(f"Quanto você pagou pelo {cont}º CD? R$"))
    gasto += valor
media = gasto/cds
print(f"Você tem {cds}CDS")
print(f"A média de seus gastos com CD's é de R${media}.")
print(f"Você gastou um total de R${gasto}.")