times = ('Botafogo','Bragantino','Grêmio','Palmeiras','Flamengo','Fluminense','Atletico-MG','Athletico-PR','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Internacional','Bahia','Vasco da Gama','Santos','Goiás','América-MG','Coritiba')
classificacao = int(input('Digite a posição que eu direi qual time esta nela no dia de hoje (8/10/2023): '))
if classificacao < 1 or classificacao > 20:
    print('Posição invalida')
else:
    print(f'Em {classificacao}º lugar temos o {times[classificacao-1]}')
    print()
    for i in range(1,21):
        if i == classificacao:
            print(f'\033[31m{i}º {times[i-1]}\033[m')
        else:
            print(f'{i}º {times[i-1]}')