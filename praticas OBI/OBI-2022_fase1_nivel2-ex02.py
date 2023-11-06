figuras = {
    'A': 10,
    'J':11,
    'Q':12,
    'K':13
}

primeira_jogada = input()
naipe_dominante = primeira_jogada[-1]

pontos_luana = 0
pontos_edu = 0
for jogad in range(6):
    jogada = input()
    if jogad < 3:
        if jogada[-1] == naipe_dominante:
            pontos_luana += figuras[jogada[0]] + 4
        else:
            pontos_luana += figuras[jogada[0]]
    else:
        if jogada[-1] == naipe_dominante:
            pontos_edu += figuras[jogada[0]] + 4
        else:
            pontos_edu += figuras[jogada[0]]

if pontos_edu > pontos_luana:
    print('Edu')
elif pontos_luana > pontos_edu:
    print('Luana')
else:
    print('Empate')