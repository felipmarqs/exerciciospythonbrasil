#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). DEpois disso, você deve mostrar para cada palavra quais sao as suas vogais
tupla = ('feijao','arroz','salada','batata','banana','brocolis','amora')
for p in tupla:
    print(f"\n Na paralavra {p.upper()} temos ",end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')