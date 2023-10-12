palavras = ('CADERNO', 'AFIADO', 'CHUPETA', 'TATUAGEM', 'VELAS', 'MUITOS', 'STEAMROLLER', 'DAR' ,'REUNIÃO', 'MAGNETIZADO')
vogais = ('A','E', 'I', 'O', 'U')

for i in palavras:
    print(f'Na palavra {i} temos', end =' ')
    for j in i:
        for h in vogais:
            if j.find(h) != -1:
                print(h, end = ' ')
                break
            else:
                continue
    print()
    