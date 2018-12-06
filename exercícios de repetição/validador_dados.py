'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''
nome = str(input("Digite o nome: "))
while len(nome) <= 3:
    nome = str(input("Nome curto demais. Tente novamente: "))
idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Este é um número absurdo pra sua idade.Tente novamente: "))
salario = int(input("Digite seu salário: "))
while salario < 0:
    salario = int(input("Você pode até ter dívidas, mas seu salário não pode ser negativo. Tente novamente: "))
sexo = str(input("Digite o sexo: [M/F]")).strip().lower()
while sexo not in 'fm':
    sexo = str(input("Sexo inválido. Tente novamente [F/M]:")).strip()
estadoc = str(input("Digite seu estado cívil[S/C/V/D]: ")).lower().strip()
while estadoc not in 'scvd':
    estadoc = str(input("Estado Civíl inválido.Tente novamente: ")).lower().strip()