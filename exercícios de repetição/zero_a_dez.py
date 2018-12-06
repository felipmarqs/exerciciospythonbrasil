#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Digite um número de zero a dez: "))
while nota < 0 or nota > 10:
    nota = int(input("Valor inválido. DIgite um número entre zero e dez: "))
print(f"{nota} é o número que você digitou.")