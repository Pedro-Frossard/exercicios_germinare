palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite outra palavra: ')
palavra3 = input('Digite mais uma palavra: ')
palavra4 = input('Digite mais outra palavra: ')
palavra5 = input('Digite outra palavra: ')
palavra6 = input('Digite a última palavra: ')
palavras = (palavra1,palavra2,palavra3,palavra4,palavra5, palavra6)
letras_iguais = 0

for indice, palavra in enumerate(palavras):
    for outra_palavra in palavras[indice+1:]:
        letras_iguais = 0
        for letra in palavra:
            tamanho_palavra = len(palavra)
            if tamanho_palavra != len(outra_palavra):
                break
            else:
                if letras_iguais == tamanho_palavra-1 and letras_iguais == len(outra_palavra)-1:
                    print(f'"{palavra}" e "{outra_palavra}" são anagramas')
                    break
                if letra in outra_palavra:
                        letras_iguais+=1
                else:
                    break
                