limite = int(input('Digite um número e eu falaeri a soma de todos os multiplos de 3 até ele: '))
acumulador = 1
contador = 0
if limite <= 0:
    print('Não há nenhum número multiplo de 3 neste intervalo')

else: 
    for i in range(0,limite+2,3):
        acumulador+=i
        contador+=1
        
    print(f'A soma dos {contador} números multiplos de 3 até {i} é igual a {acumulador}')