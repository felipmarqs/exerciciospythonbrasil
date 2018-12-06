#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turmas = int(input("Quantas turmas tem na escola? "))
soma = 0
media = 0
for c in range(1,turmas+1):
    alunos = int(input(f"Quantos alunos tem na {c}º turma? "))
    while alunos < 0 or alunos > 40:
        alunos = int(input(f"Quantos alunos tem na {c}º turma? "))
    soma += alunos
    media = soma / turmas
print(f"Essa escola tem uma média de {media} alunos. De um total de {turmas} turmas e {soma} alunos.")