# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = str(input("Em qual turno você estuda ? [M] matutino, [V] vespertino, [N] noturno: ")).lower().strip()
if turno[0] == 'm':
    print("Bom dia!")
if turno[0] == 'v':
    print("Boa tarde!")
if turno[0] == 'n':
    print("Boa noite!")
else:
    print("Inválido!")