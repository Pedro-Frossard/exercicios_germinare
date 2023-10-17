import requests

while True:
    print('Opções:\n1 --> Procurar personagens\n2 --> Procurar planetas\n3 --> Filmes\n4 --> Procurar especies\nOutro número --> Acabar a pesquisa')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        resposta = requests.get(f'https://swapi.dev/api/people/?search={input("Personagem: ")}')
        jsonrespos = resposta.json()
        
        for personagem in jsonrespos["results"]:
            print(f'\nNome = {personagem["name"]}')
            print(f'Altura = {personagem["height"]}cm')
            print(f'Peso = {personagem["mass"]}kg')
            print(f'Cor de cabelo = {personagem["hair_color"]}')
            print(f'Cor da pele = {personagem["skin_color"]}')
            print(f'Cor do olho = {personagem["eye_color"]}')
            print(f'Nascimento = {personagem["birth_year"]}')
            print(f'Genero = {personagem["gender"]}')
            if len(personagem['species']) == 0:
                print('Specie = Humano')
            else:
                resposta_specie = requests.get(personagem['species'][0])
                resposta_specie_json = resposta_specie.json()
                print(f'Specie = {resposta_specie_json["name"]}')
            if len(personagem['starships']) == 0:
                print('Nave = nenhuma')
            else:
                for numero_nave, nave in enumerate(personagem["starships"]):
                    resposta_nave = requests.get(nave)
                    resposta_nave_json = resposta_nave.json()
                    print(f'Nave {numero_nave+1} = {resposta_nave_json["name"]}')
            
            planeta = personagem['homeworld']
            resposta_planeta = requests.get(planeta)
            resposta_planeta_json = resposta_planeta.json()
            print(f'Planeta natal = {resposta_planeta_json["name"]}')
            print()
            for numero_filme, filme in enumerate(personagem['films']):
                resposta_filme = requests.get(filme)
                resposta_filme_json = resposta_filme.json()
                print(f"Filme {numero_filme+1} = {resposta_filme_json['title']}")
            print()
    elif escolha == 2:
        resposta = requests.get(f'https://swapi.dev/api/planets/?search={input("Planeta: ")}')
        jsonrespos = resposta.json()

        for resposta_planeta_json in jsonrespos['results']:
            print(f'\nPeríodo de rotação = {resposta_planeta_json["rotation_period"]} horas')
            print(f'Período de orbita = {resposta_planeta_json["orbital_period"]} dias')
            print(f'Diametro = {resposta_planeta_json["diameter"]}km')
            print(f'Terreno = {resposta_planeta_json["terrain"]}')
            print(f'Clima = {resposta_planeta_json["climate"]}')
            print(f'População = {resposta_planeta_json["population"]} pessoas\n')
            print(f'Personagens que tem como planeta natal {resposta_planeta_json["name"]}')
            for residente in resposta_planeta_json['residents']:
                resposta_residente = requests.get(residente)
                resposta_residente_json = resposta_residente.json()
                print(resposta_residente_json['name'])
            print()

    elif escolha == 3:
        resposta = requests.get(f'https://swapi.dev/api/films/?search={input("Filme: ")}')
        jsonrespos = resposta.json()
        
        for filme in jsonrespos['results']:
            print(f'Titulo = {filme["title"]}')
            print(f'Lançamento = {filme["release_date"]}')
            print(f'\nPersonagens que participaram do filme')
            for personagem_filme in filme['characters']:
                resposta_personagem = requests.get(personagem_filme)
                jsonrespos_personagem = resposta_personagem.json()
                print(jsonrespos_personagem['name'])
    elif escolha == 4:
        resposta = requests.get(f'https://swapi.dev/api/species/?search={input("Especie: ")}')
        jsonrespos = resposta.json()

        for specie in jsonrespos['results']:
            print(f'Nome = {specie["name"]}')
            print(f'Classificação = {specie["classification"]}')
            print(f'Altura média = {specie["average_height"]}cm')
            print(f'Cor da pele = {specie["skin_colors"]}')
            print(f'Cor de olho = {specie["eye_colors"]}')
            print(f'Cor de cabelo = {specie["hair_colors"]}')

            habitacao = requests.get(specie['homeworld'])
            habitacao_json = habitacao.json()
            print(f'Planeta habitado = {habitacao_json["name"]}')
            print(f'Lingua = {specie["language"]}')
            print(f'\nPersonagens desta especie')
            for personagen_especie in specie['people']:
                resposta_especie = requests.get(personagen_especie)
                jsonrespos_especie = resposta_especie.json()
                print(jsonrespos_especie['name'])
    else:
        print('Acabou!')
        break
    




