def criptografarChave(mensagem,chave):
    if chave >= 0 or chave <=25:
        contador = 0
        mensagem_criptografada = ''
        while contador < len(mensagem):
            
            letra = mensagem[contador]
            contador+=1
            letra_alfabeto = alfabeto.find(letra)
            if letra_alfabeto + chave > 25:
                letra_alfabeto -= 25
                letra_criptografada = alfabeto[letra_alfabeto+chave]
            else:
                letra_criptografada = alfabeto[letra_alfabeto+chave]
            mensagem_criptografada +=letra_criptografada
        print(f'A mensagem criptografada com a chave {chave} é {mensagem_criptografada}')


    else:
        print('Digite uma chave entre 0 e 25')
def decodificarChave(mensagem, chave):
    if chave >= 0 or chave <=25:
        mensagem_decodificada = ''
        contador = 0 
        while contador < len(mensagem):
            letra = mensagem[contador]
            contador+=1
            letra_alfabeto = alfabeto.find(letra)
            if letra_alfabeto - chave < 0:
                    letra_alfabeto += 25
                    letra_decodificada = alfabeto[letra_alfabeto-(chave - 1)]
                    mensagem_decodificada +=letra_decodificada
            else:
                    letra_decodificada = alfabeto[letra_alfabeto-chave]
                    mensagem_decodificada +=letra_decodificada
        print(f'A mensagem decodificada com a chave {chave} é {mensagem_decodificada}')
# dentro de um if
mensagem_criptografada = ''
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
tamanho_alfabeto = len(alfabeto)
chave = int(input('Digite uma chave para a criptografia: '))
mensagem = input('Digite a mensagem a ser criptografada: ')

decodificarChave(mensagem, chave)







    