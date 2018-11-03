#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda note: "))
n3 = float(input("Informe a terceira nota: "))
m = (n1 + n2 + n3) / 3
if m >= 7 and m <= 9.99:
    print(f"A média do aluno foi {m:.2f} e ele foi APROVADO!")
elif m < 7:
    print(f"A média do aluno foi {m:.2f} e ele foi REPROVADO!")
elif m == 10:
    print(f"A média do aluno foi {m} e ele foi aprovado com DISTINÇÃO! PARABÉNS!!!")
