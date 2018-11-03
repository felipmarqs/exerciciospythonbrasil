'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. '''
o = str(input("Quer \n"
              "Gasolina[G]\n"
              "Alcóol[A]\n"
              "Qual?")).strip().lower()
if o[0] == 'g':
    l = int(input("Quantos litros vocês deseja botar ?"))
    if l < 20:
       d = ((l * 4) / 100)
       p = (l * 2.5) - d

       print(f"{l} Litros \n"
             f"{d * 100}% de desconto \n"
             f"R${l} valor sem desconto \n"
             f"R${p} valor com desconto ")
