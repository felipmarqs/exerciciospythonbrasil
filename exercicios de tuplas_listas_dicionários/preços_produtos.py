#crie um programa que tenha uma tupla única com nomes e produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços organizando os dados em forma tabular.
produtos = ('Banana', 1.99,
            'Café', 8.75,
            'Água 2L', 2.99,
            'Arroz', 10.50,
            'Sorvete', 17.50)
for p in produtos:
    if produtos.index(p) % 2 == 0:
        print(f"{p:.<35}",end='R$ ')
    else:
        print(f"{p:>2}")