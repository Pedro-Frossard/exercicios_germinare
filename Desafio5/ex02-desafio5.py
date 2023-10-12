contador = lucas = wellington = gabriella = 0
while True:
    print('VOTAÇÃO:\n[1] Lucas\n[2] Wellington\n[3] Gabriella\n[4] Voto em branco')
    voto = int(input('Sua escolha: '))
    sair = input('Todos ja votaram? [S/N] ').upper()
   
    if voto < 4 and voto > 0:
        contador += 1
        if voto == 1:
            lucas+=1
        elif voto == 2:
            wellington+=1
        elif voto == 3:
            gabriella+=1
    if sair.startswith('N'):
        continue 
    
    else:
        if max(lucas,gabriella,wellington) == lucas and max(lucas,gabriella,wellington) == wellington:
            print(f'RESULTADOS:\nNúmero de votos validos {contador}\nEMPATE entre Lucas e Wellington')
            break
        elif max(lucas,gabriella,wellington) == lucas and max(lucas,gabriella,wellington) == gabriella:
            print(f'RESULTADOS:\nNúmero de votos validos {contador}\nEMPATE entre Lucas e Gabriella')
            break
        elif max(lucas,gabriella,wellington) == wellington and max(lucas,gabriella,wellington) == gabriella:
            print(f'RESULTADOS:\nNúmero de votos validos {contador}\nEMPATE entre Gabriella e Wellington')
            break
        elif max(lucas,gabriella,wellington) == gabriella and max(lucas,gabriella,wellington) == lucas and max(lucas,gabriella,wellington) == wellington:
            print(f'RESULTADOS:\nNúmero de votos validos {contador}\nEMPATE, todos os votos foram iguais')
            break

        else:
            if lucas > wellington and lucas > gabriella:
                ganhador = 'Lucas'
            elif wellington > lucas and wellington >gabriella:
                ganhador = 'Wellington'
            elif gabriella > lucas and gabriella > wellington:
                ganhador = 'Gabriella'
            print(f'RESULTADOS:\nNúmero de votos validos {contador}\nGANHADOR --> {ganhador} que ganhou com {max(lucas,wellington,gabriella)*100/contador:.2f}%')
            break


