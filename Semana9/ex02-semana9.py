num_de_alunos = int(input('Quantos alunos tem na turma? '))
informacoes_alunos = []
contador = 0
if num_de_alunos <= 0:
    print('O número de alunos não existe')
else: 
    while contador < num_de_alunos:
        nome = input(f'Qual é o nome do {contador+1}º aluno? ')
        nota1 = float(input(f'Qual foi a 1º nota de {nome}? '))
        nota2 = float(input(f'Qual foi a 2º nota de {nome}? '))
        if nota1 > 10 or nota1<0 or nota2>10 or nota2<0:
            print('Notas invalidas')
            continue
        media = (nota1+nota2)/2
        informacoes_alunos.append([nome,nota1,nota2,media])
        if media >= 7.0:
            informacoes_alunos[contador].append('Aprovado')
        else:
            informacoes_alunos[contador].append('Reprovado')
        contador+=1
    print(f'N: {" ":<3}Alunos:{" ":^5}Nota 1:{" ":^5}Nota 2:{" ":^5}Média:{" ":^5}Conceito:')
    for numero, aluno in enumerate(informacoes_alunos):
        print(f'{numero+1:<6}', end='')
        for informacao in aluno:
            print(f'{informacao:<12}', end='')
        print()
