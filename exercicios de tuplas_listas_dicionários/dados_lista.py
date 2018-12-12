#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantoss números foram digitados. B) A lista de valores ordenada de forma descrescente. C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
continuar = 's'
while True:
    lista.append(int(input("Digite um número: ")))
    continuar = str(input("Deseja continuar [S/N]: ")).strip().lower()
    if continuar in 's':
        print("Valor adicionado com sucesso!")
    elif continuar in 'n':
        break
print(f"Foram adicionados {count(lista)} valores á lista.")
print(f"A lista em ordem descrescente é {reversed(lista)} ")
print(f"{lista.index(5)}")