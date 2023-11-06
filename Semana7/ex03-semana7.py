alunos_business = int(input('Quantos alunos tem a Escola Germinare Business? '))
alunos_TECH = int(input('Quantos alunos tem a Escola Germinare TECH? '))


if alunos_business > alunos_TECH:
    for i in range(1,10000):
        alunos_business*=1.10
        alunos_TECH*=1.50
        if alunos_TECH > alunos_business:
            print(f'Com este número de alunos em cada uma das escolas,\na Escola Germinare TECH ultrapassará a Escola Germinare Business em termo de alunos em {i} anos')
            break

else:
    print('De acordo com os dados que você me forneceu, a Escola Germinare TECH já tem mais alunos que a Escola Germinare Business')
