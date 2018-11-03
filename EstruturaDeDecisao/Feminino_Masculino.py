#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sex = str(input("[F ou M ?]")).lower()
if sex == 'f':
    print("Sexo feminino")
elif sex == 'm':
    print("Sexo masculino")
else:
    print("Inválido!")
