def contarLetras(palavra):
    letras = dict()
    for letra in palavra:
        if letra in letras.keys():
            continue
        letras[letra] = palavra.count(letra)
    return letras



palavra = input('Digite uma palavra: ')
contarLetras(palavra)
for letra in contarLetras(palavra).items():
    if letra[1] > 1:
        print(f'Letra {letra[0]} aparece {letra[1]} vezes')
    else:
        print(f'Letra {letra[0]} aparece {letra[1]} vez')