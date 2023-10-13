print('Olá, seja bem-vindo(a)\nDigite o nome, idade e cidade de 5 estudantes:')
estudantes = set()

for i in range(5):
    print(f'Estudante {i+1}:')
    nome = input('Nome: ').title()
    idade = int(input('Idade: '))
    if idade <= 0:
        print('Digite uma idade válida')
        break
    cidade = input('Cidade: ').title()
    informacoes = (nome, idade, cidade)
    estudantes.add(informacoes)

if idade > 0:
    grupos = set()
    for estudante in estudantes:
        grupo = {estudante[0]}
        for outro_estudante in estudantes:
            if estudante != outro_estudante and estudante[1] == outro_estudante[1] and estudante[2] == outro_estudante[2]:
                grupo.add(outro_estudante[0])
        grupos.add(tuple(grupo))
    
    contador = 0
    for grupo in grupos:
        contador += 1
        print(f'\nGrupo {contador}:')
        for i in grupo:
            print(f'{i}', end = ' ')
