#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
mb = float(input("Qual o tamanho do arquivo que você deseja baixar em MB?"))
mbps = int(input("Qual a velocidade da sua internet em MBPS ?"))
t = mb / mbps
minutos = t / 60
print(f"Para baixar {mb} MB vai levar {minutos:.2f} minutos ")