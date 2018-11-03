'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

      O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''
n1 = float(input("Digite uma nota do aluno: "))
n2 = float(input("Digite outra nota do aluno: "))
m = (n1+n2)/2
print(m)
if m < 3.9:
    print("O aluno ficou com média E")
elif m > 4 and m < 5.9:
    print("O aluno ficou com média D")
elif m > 6 and m < 7.5:
    print("O aluno ficou com média C")
elif m > 7.6 and m < 8.9:
    print("O aluno ficou com média B")
elif m > 9 and m <= 10:
    print("O aluno ficou com média A")

#Deu errado