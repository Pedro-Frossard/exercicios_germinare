from random import randint

valores = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram:', end = ' ')
for i in range(5):
    print(f'{valores[i]}', end = ' ')
print()
print(f'O maior valor sorteado foi {max(valores)}\nO menor valor sorteado foi {min(valores)}')
