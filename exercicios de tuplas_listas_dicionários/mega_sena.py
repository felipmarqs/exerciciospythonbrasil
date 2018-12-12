#Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print("APOSTE NA MEGA-SENA")
print("-=" *30)
palpites = int(input("Quantos palpites você quer gerar ? "))
lista = []
dado = []
for c in range(0,palpites):
    for r in range(0,6):
        dado.append(randint(0,61))
    lista.append(dado[:])
    print(f"Jogo {c+1}: {dado} ")
    dado.clear()
    sleep(1)
print("-="*30)
print("BOA SORTE!!!")