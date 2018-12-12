#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoas em um dicionário e todos os dicionários em uma lista. No final, mostre: Quantas pessoas foram cadastradas. A média de idade do grupo. Uma lista com todas as mulheres. Uma lista com todas as pessoas com idade acima da média.
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
        print("Erro! Responda apenas S ou N." )
    if resp == 'N':
        break
print("-="*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A media de idade é de {media:5.2f} anos")
print("-=" * 30)
print("C) As mulheres cadastradas foram: ")
for p in galera:
    if p['sexo'] in 'fF':
        print(f"{p['nome']}",end='')
print()
print("D) Lista de pessoas que estão acima da média: ",end='')
for a in galera:
    if a['idade'] >= media:
        print('        ')
        for k,v in a.items():
            print(f"{k} = {v}",end=';')
        print()
print("!!!!FIM!!!!")