#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = str(input("Digite um nome de usuário: ")).strip()
senha = str(input("Digite uma senha: "))
while senha == usuario:
    print("Os valores de usuário e senha não podem ser iguais!")
    usuario = str(input("Digite um nome de usuário: "))
    senha = str(input("Digite uma senha: "))
print("Dados validados com sucesso!")
