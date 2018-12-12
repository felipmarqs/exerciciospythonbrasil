alunos = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome,[nota1,nota2],media])
    resp = str(input("Quer continuar ? [S/N]")).lower().strip()
    if resp in 'n':
        break
print("-=" *30)
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
print("-=" *30)
for i,a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.3}')
print("-=" *30)
while True:
    print('-' *35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]}")
    print("Volte sempre!")