'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''
from math import sqrt
print("Informe os valores de ax² + bx + c")
a = float(input("O valor de a: "))
if a == 0:
    print("Não é uma equação de primeiro grau.")
else:
    b = float(input("O valor de b: "))
    c = float(input("O valor de c: "))
    delta = ((b)**2) - (4*(a)*(c))
    x1 = ((- b) + (sqrt(delta))) / (2* (a))
    x2 = ((- b) - (sqrt(delta))) / (2* (a))
    if delta < 0:
        print("O delta é negativo! Programa encerrado!")
    elif delta == 0:
        print(f"O delta é = 0 ,então tem apenas uma raiz real que é {x1}")
    else:
        print(f"O valor de x' é {x1} e de x'' é {x2}.")