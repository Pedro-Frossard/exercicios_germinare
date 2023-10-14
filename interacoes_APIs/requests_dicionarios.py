import requests

resposta = requests.get(f'https://swapi.dev/api/people/?search={input("personagem: ")}')
jsonrespos = resposta.json()
personagens = jsonrespos["results"]

print(f'Foram encontrados {len(jsonrespos["results"])} personagens')

for personagem in jsonrespos["results"]:
    print(f'Nome = {personagem["name"]}')
    print(f'Altura = {personagem["height"]}cm')
    print(f'Peso = {personagem["mass"]}kg')
    
    for nave in personagem["starships"]:
        resposta = requests.get(nave)
        resposta_json = resposta.json()
        print(f'Nome da nave: {resposta_json["name"]}')
    print()




