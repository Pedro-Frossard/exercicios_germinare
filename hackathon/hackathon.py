import requests
import json
from fpdf import FPDF
from math import ceil


pessoas = dict()
def gerandoPDF():
    pdf = FPDF() #Essa linha cria uma variável que vai armazenar as informações da função FPDF da biblioteca
    pdf.add_page() #Essa linha cria uma página em PDF, em branco ainda.
    pdf.set_font("Arial", size=12) #Essa linha é definida que os textos irão aparecer na fonte Arial e no tamanho de 20pt (lembra do word? igual.)
    segmento_indicado = []
    ativo_indicado = []
    #ativos para cliente arrojado
    for ativo in ativos:
        rentabilidade = ativo['preco']*(dys[ativo['ticker']]/100)
        if ativo['segmento'] not in segmento_indicado:
            if rentabilidade > 7:
                segmento_indicado.append(ativo['segmento'])
                ativo_indicado.append(ativo)
            if len(segmento_indicado) == 5:
                break
    for ativo in ativos:
        rentabilidade = ativo['preco']*(dys[ativo['ticker']]/100)
        if ativo['segmento'] == 'FII' and rentabilidade > 5 and rentabilidade < 9:
            ativo_FII_moderado = ativo
            break
    for ativo in ativos:    
        rentabilidade = ativo['preco']*(dys[ativo['ticker']]/100)
        if ativo['segmento'] != 'FII' and rentabilidade > 5 and rentabilidade < 9:
            ativo_moderado = ativo
            break
    for ordem, ativo in enumerate(ativos):
        rentabilidade = ativo['preco']*(dys[ativo['ticker']]/100)
        if rentabilidade < 4:
            if ordem == 0:
                maior_dy = rentabilidade
                ativo_maior_dy = ativo
            else:
                maior_dy = max(rentabilidade, maior_dy)
                if maior_dy == rentabilidade:
                    ativo_maior_dy = ativo
        
    texto = f'''Ações recomendadas para o perfil de arrojado:
Ativo 1:
Data: {ativo_indicado[0]['data']}
Ticker: {ativo_indicado[0]['ticker']}
Preço: {ativo_indicado[0]['preco']}
Segmento: {ativo_indicado[0]['segmento']}

Ativo 2:
Data: {ativo_indicado[1]['data']}
Ticker: {ativo_indicado[1]['ticker']}
Preço: {ativo_indicado[1]['preco']}
Segmento: {ativo_indicado[1]['segmento']}

Ativo 3:
Data: {ativo_indicado[2]['data']}
Ticker: {ativo_indicado[2]['ticker']}
Preço: {ativo_indicado[2]['preco']}
Segmento: {ativo_indicado[2]['segmento']}

Ativo 4:
Data: {ativo_indicado[3]['data']}
Ticker: {ativo_indicado[3]['ticker']}
Preço: {ativo_indicado[3]['preco']}
Segmento: {ativo_indicado[3]['segmento']}

Ativo 5:
Data: {ativo_indicado[4]['data']}
Ticker: {ativo_indicado[4]['ticker']}
Preço: {ativo_indicado[4]['preco']}
Segmento: {ativo_indicado[4]['segmento']}



Ação para cliente moderado:
Data: {ativo_moderado['data']}
Ticker: {ativo_moderado['ticker']}
Preço: {ativo_moderado['preco']}
Segmento: {ativo_moderado['segmento']}

Fundo imobiliario para cliente moderado:
Data: {ativo_FII_moderado['data']}
Ticker: {ativo_FII_moderado['ticker']}
Preço: {ativo_FII_moderado['preco']}
Segmento: {ativo_FII_moderado['segmento']}



Maior DY para cliente conservador:
Data: {ativo_maior_dy['data']}
Ticker: {ativo_maior_dy['ticker']}
Preço: {ativo_maior_dy['preco']}
Segmento: {ativo_maior_dy['segmento']}
'''
    largura_maxima = pdf.w - 2 * pdf.l_margin
    largura_texto = pdf.get_string_width(texto)
    num_linhas = ceil(largura_texto / largura_maxima)
    pdf.multi_cell(w=largura_maxima, h=pdf.font_size, txt=texto)
    pdf.output('Relatorio.pdf')
def fazerCadastro():
    while True:
        nome = input('Nome completo: ').title()
        if nome.find(' ') == -1:
            print('Digite seu nome completo: ')
            continue
        else:
            while True:
                data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
                if len(data_nascimento) < 10:
                    print('Data invalida')
                    continue
                else:
                    break
        break
    print('''\nQual é o seu perfil?
        • 1 - Conservador: está disposto a renunciar a rentabilidade em troca de mais segurança
e liquidez. Logo, produtos de renda fixa, com rentabilidade previsível, são mais
adequados para esse tipo de perfil.
        • 2 - Moderado: Esse investidor está entre os conservadores e os arrojados. Ele gosta de
segurança, mas já possui tolerância a riscos de longo prazo. Assim, opta por
investimentos mais arriscados dependendo da situação.
        • 3 - Arrojado: Esse perfil de investidor entende que as perdas a curto prazo são
momentâneas e necessárias para aproveitar lucros mais altos a longo prazo.
''')
    while True:
        perfil_investidor = int(input('Qual é o seu perfil? '))
        if perfil_investidor == 1:
            pessoas[nome] = [data_nascimento, 'conservador']
            for chave in pessoas.keys():
                if chave == nome:
                    print(f'{nome}:\nData de nascimento: {pessoas[nome][0]}\nPerfil: {pessoas[nome][1]}')
                    break
            break
        elif perfil_investidor == 2:
            pessoas[nome] = [data_nascimento, 'moderado']
            for chave in pessoas.keys():
                if chave == nome:
                    print(f'{nome}:\nData de nascimento: {pessoas[nome][0]}\nPerfil: {pessoas[nome][1]}')
                    break
            break
        elif perfil_investidor == 3:
            pessoas[nome] = [data_nascimento, 'arrojado']
            for chave in pessoas.keys():
                if chave == nome:
                    print(f'Nome: {nome}\nData de nascimento: {pessoas[nome][0]}\nPerfil: {pessoas[nome][1]}')
                    break
            break
        else:
            print('Perfil invalido, tente novamente')
            continue

def montarDados():
    for ordem, ativo in enumerate(ativos):
        rentabilidade = ativo['preco']*(dys[ativo['ticker']]/100)
        if ordem == 0:
            maior_rentabilidade = rentabilidade
            ativo_maior_rentabilidade = ativo
            
        else:
            maior_rentabilidade = max(maior_rentabilidade, rentabilidade)
            if maior_rentabilidade == rentabilidade:
                ativo_maior_rentabilidade = ativo
    print(f'O ativo de maior rentabilidade foi:\nTicker: {ativo_maior_rentabilidade["ticker"]}\nPreço: {ativo_maior_rentabilidade["preco"]}\nData: {ativo_maior_rentabilidade["data"]}\nSegmento: {ativo_maior_rentabilidade["segmento"]}\n')
    segmentos = {'Saude' : 0 ,'Energia' : 0 ,'FII' : 0 ,'Varejo' : 0 ,'Alimento' : 0}
    for segmento in segmentos.keys():
        segmento_encontrado = 0
        for ativo in ativos:
            if ativo['segmento'] == segmento:
                segmento_encontrado+=1
                segmentos[segmento]+= ativo['preco']*(dys[ativo['ticker']]/100)
        segmentos[segmento] = segmentos[segmento]/segmento_encontrado
    segmento_maior_rentabilidade = max(segmentos['Alimento'],segmentos['Energia'], segmentos['FII'], segmentos['Saude'], segmentos['Varejo'])
    for segmento in segmentos:
        if segmentos[segmento] == segmento_maior_rentabilidade:
            print(f'O segmento de maior rentabilidade foi o {segmento}\n')
            break
    for segmento in segmentos:
        print(f'De acordo com a média do segmento {segmento} que foi {segmentos[segmento]:.2f}\nComparando com a selic:{segmentos[segmento]-12.75}%')
    
    


resposta_ativos = requests.get('https://github.com/germinatech/base_hackathon/blob/main/ativos.json')

resposta_ativos = resposta_ativos.json()

ativos = json.loads(resposta_ativos['payload']['blob']['rawLines'][0])

resposta_dy = requests.get('https://github.com/germinatech/base_hackathon/blob/main/dy.json')

resposta_dy = resposta_dy.json() 

dys = json.loads(resposta_dy['payload']['blob']['rawLines'][0])

while True:
    print('Opções\n[1] Novo cadastro\n[2] Mostrar dados dos ativos\n[3] Encerrar e criar relatorio')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        fazerCadastro()
    elif escolha == 2:
        montarDados()
    elif escolha == 3:
        print('Encerrando')
        gerandoPDF()
        break
    else:
        print('Digite uma opção valida')
        continue