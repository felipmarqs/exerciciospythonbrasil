#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
a = int(input("Informe a população da cidade A: "))
b = int(input("Informe a população da cidade B: "))
ta = float(input("Informe a taxa de crescimento da cidade A em %: "))
tb = float(input("Informe a taxa de crescimento da cidade B em %: "))
cont = 0
while a != b:
    a += a * (ta/100)
    b += b * (tb/100)
    cont += 1
print(f"A cidade A ultrapassa ou iguala a população de B em {cont} anos")