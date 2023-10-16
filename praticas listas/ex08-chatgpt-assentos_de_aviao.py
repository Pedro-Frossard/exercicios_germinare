from random import randint

def Passagem_aerea(acentos):
    lugares = []
    pessoas = int(input('Quantas pessoas vão na viagem? '))
    for lugar in range(pessoas):
        lugares.append([0,0])
    contador = 0
    while contador < pessoas:
        linha_passagem = int(input(f'Qual é a linha que o {contador+1}º passageiro vai ficar? '))
        coluna_passagem = int(input('E qual a coluna? '))
        contador+=1
        if linha_passagem-1 > linhas_aviao-1 or coluna_passagem-1 > colunas_aviao-1:
            print('Linha ou coluna invalida\nTente novamente!')
            contador-=1
            continue
        if acentos[linha_passagem-1][coluna_passagem-1] != 'O':
            print('O lugar está ocupado\nTente novamente!')
            contador-=1
            continue
        else:
            lugares[contador-1][0] = linha_passagem
            lugares[contador-1][1] = coluna_passagem
            acentos[(lugares[contador-1][0])-1][(lugares[contador-1][1])-1] = '\033[32mX\033[m'
    print('Compra feita com sucesso! Boa viagem!\n')
    for x in acentos:
        for n in x:
            print(f'[{n}]', end='')
        print()


colunas_aviao = int(input('Quantas colunas tem os acentos do avião: '))
linhas_aviao = int(input('Quantas linhas tem o avião: '))

acentos = []
for acento in range(linhas_aviao):
    acentos.append(['O']* colunas_aviao)
print('Neste momento o avião está assim\n\nX --> OCUPADO\nO --> LIVRE\n')


for ocupado in range(round(linhas_aviao*colunas_aviao/2)):
    acentos[randint(0,linhas_aviao-1)][randint(0,colunas_aviao-1)] = 'X'

for x in acentos:
    for n in x:
        print(f'[{n}]', end='')
    print()

Passagem_aerea(acentos)