#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final mostre:  A) QUantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leve.
pessoas = list()
pesadas = list()
leves = list()
dado = list()
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input("Deseja continuar ?[S/N]: ")).strip().lower()
    if continuar in 'n':
        break

for p in pessoas:
    if p[1] > 90:
        pesadas += p[:]
    elif p[1] < 89:
        leves += p[:]
print(f"Foram registradas {len(pessoas)} pessoas.")
print("As pessoas consideradas pesadas são: ")
for p in pesadas:
    print(f"{p[:]} com {p[:]} Kgs")
print("As pessoas consideradas leves são: ")
for l in leves:
    print(f"{l[:]} com {l[:]} Kgs")