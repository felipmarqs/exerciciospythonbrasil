#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de zero. o dicionário também receberá o ano de contratação e o salário. Calcule e acrescente. além da idade, com quantos a pessoa vai se aposentar.
from datetime import date
funcionário = dict()
funcionário['nome'] = str(input("Digite o nome do funcionário: ")).capitalize()
funcionário['nascimento'] = int(input("Digite o ano de nascimento: "))
funcionário['idade'] = date.today().year - funcionário['nascimento']
funcionário['CTPS'] = int(input("Carteira de trabalho(0 não tem): "))
if funcionário['CTPS'] != 0:
    funcionário['contratação'] = int(input("Ano de contratação: "))
    funcionário['salario'] = float(input("Salário: R$"))
    contribuição = date.today().year - funcionário['contratação']
    funcionário['aposentadoria'] = (funcionário['contratação'] + 35) - date.today().year + funcionário['idade']
for k,v in funcionário.items():
    print(f"- {k} tem o valor {v}.")
