alunos = int(input('Quantos alunos tem na sala? '))
contador = maior_media = menor_media = aprovado = reprovado = 0
while True:
    contador+=1
    nome_aluno = input(f'Qual é o nome do {contador}º aluno? ')
    nota1 = float(input(f'Qual foi a primeira nota de {nome_aluno}? '))
    nota2 = float(input(f'Qual foi a segunda nota de {nome_aluno}? '))
    nota3 = float(input(f'Qual foi a terceira nota de {nome_aluno}? '))
    if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
        print('Digite uma nota valida')
        contador-=1
        continue
    else:
        media = (nota1*0.2 + nota2*0.3 + nota3*0.5)
        print(f'A média final de {nome_aluno} foi de {media:.2f}, deseja passar para o proximo aluno(a)?')
        continuar = input('S/N: ').lower()
        if continuar.startswith('n'):
            contador-=1
            continue
        else:
            if media >= 7:
                aprovado+=1
            elif media < 7:
                reprovado+=1
            if contador == 1:
                menor_media = maior_media = media
                aluno_menor_media = aluno_maior_media = nome_aluno
            elif contador > 1:
                menor_media = min(menor_media,media)
                maior_media = max(maior_media,media)
                if menor_media ==  media:
                    aluno_menor_media = nome_aluno
                elif maior_media == media:
                    aluno_maior_media = nome_aluno
        if contador >= alunos:
            print(f'A turma teve:\n- Aprovados: {aprovado} --> {aprovado*100/alunos:.2f}%\n- Reprovados: {reprovado} --> {reprovado*100/alunos:.2f}%\nMaior média: {maior_media:.2f} do aluno(a) {aluno_maior_media}\nMenor média: {menor_media:.2f} do aluno(a) {aluno_menor_media}')    
            break
        
