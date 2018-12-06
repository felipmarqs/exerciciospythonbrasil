#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
continuar = 's'
maior = menor = 0
cont = 0
while continuar == 's':
    temperatura = int(input("Informe a temperatura: ºC "))
    if cont == 0:
        menor = temperatura
    elif temperatura > maior:
        maior = temperatura
    elif temperatura< menor:
        menor = temperatura
    continuar = str(input("Deseja continuar? [S/N]")).strip().lower()
    cont += 1
print(f"Dos {cont} valores de temperatura que você digitou, o maior foi {maior} e o menor foi {menor}.")