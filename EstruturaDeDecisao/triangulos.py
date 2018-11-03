'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; '''

print("Digite os lados de um tringulo")
l1 = int(input("lado um: "))
l2 = int(input("lado dois: "))
l3 = int(input("lado três: "))

if l1 == l2 == l3:
    print("É um triângulo equilátero!")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("É um triângulo isósceles!")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("É um triângulo escaleno!")