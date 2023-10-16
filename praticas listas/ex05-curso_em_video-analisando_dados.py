pesos = []
nomes = []
while True:
    nome = input('Nome: ')
    nomes.append(nome)
    peso = float(input('Peso: '))
    pesos.append(peso)
    sair = input('Deseja sair? ').lower()
    if sair.startswith('s'):
        maior_peso = max(pesos)
        menor_peso = min(pesos)
        for informacoes in zip(nomes, pesos):
            if maior_peso == informacoes[1]:
                print(f'O maior peso registrado foi do(a) {informacoes[0]} que pesa {informacoes[1]}kg')
            elif menor_peso == informacoes[1]:
                print(f'O menor peso registrado foi do(a) {informacoes[0]} que pesa {informacoes[1]}kg')
        break