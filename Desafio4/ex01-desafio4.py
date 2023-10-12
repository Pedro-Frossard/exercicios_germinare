from datetime import date

primeiro_salario=float(input('Qual foi o seu primeiro salario na JBS? R$'))
ano_contratacao=int(input('Digite o ano em que você foi contratado(a): '))
ano_hoje = date.today().year
if primeiro_salario < 1000:
    print('Digite um salario acima de R$1000')
if 1995 > ano_contratacao or ano_contratacao >= ano_hoje:
    print('Digite um ano entre 1995 e o ano atual\nSe você foi contratado(a) este ano, ainda não tem almento')

aumento = primeiro_salario*1.015
diferença_anos=ano_hoje-ano_contratacao
contador = 1
while diferença_anos > contador:
    aumento_total=aumento*1.10
    aumento=aumento_total
    contador+=1
    
print(f'Depois de {diferença_anos} anos trabalhando na JBS você ganhou um aumento de R${aumento_total:.2f}')