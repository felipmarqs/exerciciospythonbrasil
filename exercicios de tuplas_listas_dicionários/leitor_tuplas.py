#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: A) Quantas vezes apareceu o valor 9; B) Em que posição foi digitado o primeiro valor 3.;C0 Quais foram os números pares.
tupla= (int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")))
print(f"Você digitou os valores {tupla}")
print(f"O número 9 foi digitado {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O primeiro valor 3 foi digitado na posição {tupla.index(3)}")
else:
    print("O valor 3 não foi digitado!")
print("Os valores pares digitados foram", end= ' ')
for n in tupla:
    if n % 2 == 0:
        print(n,end = ' ')
