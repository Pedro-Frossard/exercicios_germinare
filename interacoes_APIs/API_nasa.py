import requests
from datetime import date, timedelta

data_hoje = date.today()

amanha = data_hoje + timedelta(days=1)

key = 'e28d8EqNKm9KsajHlkNeAC2iv7DK7DyFJv05fuCX'
def imagem_do_dia():
    resposta_imagem = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    resposta_imagem = resposta_imagem.json()
    print(f'\n{resposta_imagem["title"]:^80}\n{resposta_imagem["date"]:^80}\n\nImagem: {resposta_imagem["url"]}\n\nDescrição: {resposta_imagem["explanation"]}')


def mostrarAsteroides():
    resposta_asteroide = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={date.today()}&end_date={amanha}&api_key={key}')
    resposta_asteroide = resposta_asteroide.json()
    while True:
        print('''
Menu:
1 - Todos os asteroides
2 - Asteroides grandes (mais de 200 metros)
3 - Asteroides pequenos (menos de 200 metros)
Outro número - Menu principal
''')
        escolha_asteroides = int(input('Escolha: '))
        if escolha_asteroides > 0 and escolha_asteroides < 4:
            if escolha_asteroides == 1:
                for dia in resposta_asteroide["near_earth_objects"].items():
                    for asteroide in dia[1]:
                        print(f'Nome: {asteroide["name"]}\nDiametro estimado: {asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"]:.2f} metros\nVelocidade estimada: {float(asteroide["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]):.2f} km/h')
                        if asteroide["is_potentially_hazardous_asteroid"]:
                            print('\033[1;31mPotencialmente perigoso\033[m\n')
                        else:
                            print('\033[1;32mNão é preocupante\033[m\n')

            elif escolha_asteroides == 2:
                for dia in resposta_asteroide["near_earth_objects"].items():
                    for asteroide in dia[1]:
                        if asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"] > 200:
                            print(f'Nome: {asteroide["name"]}\nDiametro estimado: {asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"]:.2f} metros\nVelocidade estimada: {float(asteroide["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]):.2f} km/h')
                            if asteroide["is_potentially_hazardous_asteroid"]:
                                print('\033[1;31mPotencialmente perigoso\033[m\n')
                            else:
                                print('\033[1;32mNão é preocupante\033[m\n')
            elif escolha_asteroides == 3:
                for dia in resposta_asteroide["near_earth_objects"].items():
                    for asteroide in dia[1]:
                        if asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"] < 200:
                            print(f'Nome: {asteroide["name"]}\nDiametro estimado: {asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"]:.2f} metros\nVelocidade estimada: {float(asteroide["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]):.2f} km/h')
                            if asteroide["is_potentially_hazardous_asteroid"]:
                                print('\033[1;31mPotencialmente perigoso\033[m\n')
                            else:
                                print('\033[1;32mNão é preocupante\033[m\n')
        else:
            break


def mostrarImagem():
    while True:
        data = input('Digite uma data no formato AAAA-MM-DD: ')
        try:
            resposta_imagem = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{data}?api_key={key}')
            resposta_imagem = resposta_imagem.json()
            if resposta_imagem == []:
                print('Nenhuma imagem para o dia fornecido, deseja continuar? ')
                continuar = input('[S/N]: ').upper()
                if continuar.startswith('N'):
                    break
            else:
                for ordem, imagem in enumerate(resposta_imagem):
                    print(f'Imagem {ordem+1}:\nLink: https://api.nasa.gov/EPIC/archive/natural/{data.replace("-","/")}/png/{imagem["image"]}.png?api_key={key}')
                break
        except:
            print('Digite a data corretamente')
            continue



while True:
    print('''
Menu:
1 - Imagem do dia
2 - Asteroides orbitando a Terra
3 - Imagens
''')
    escolha = int(input('Escolha: '))

    if escolha > 0 and escolha < 4:
        if escolha == 1:
            imagem_do_dia()
        elif escolha == 2:
            mostrarAsteroides()
        if escolha == 3:
            mostrarImagem()
    else:
        print('Fim')
        break