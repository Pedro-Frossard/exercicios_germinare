print(48*'=')
print('     10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print(48*'=')

primeiro_termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('QUal é a razão? '))
decimo_termo = primeiro_termo+10*razao
for i in range(primeiro_termo,decimo_termo,razao):
    print(f'{i} --> ',end='')

print('ACABOU')