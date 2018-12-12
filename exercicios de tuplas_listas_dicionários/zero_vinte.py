#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input("Digite um número de 0 a 20: "))
while numero < 0 or numero > 20:
    print('Valor incorreto!')
    numero = int(input("Digite um número de 0 a 20: "))
print(f"Você digitou o número {tupla[numero]}.")