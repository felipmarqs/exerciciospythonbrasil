#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
l = str(input("Digite uma letra:"))
if l in 'aeiou':
    print("Essa letra é uma vogal!")
else:
    print("Essa letra é uma consoante!")