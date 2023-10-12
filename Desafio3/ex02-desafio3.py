'''O programa deve receber o valor do empréstimo, sua renda atual e respostas para quatro
perguntas sobre o perfil de crédito. As perguntas são as seguintes:

1 - "Seu Score de crédito é acima de 450 pontos?"
2 - "Você não possui dívidas ativas?"
3 - "Você é funcionário público?"
4 - "Você concorda em compartilhar seus dados de outros bancos através do open banking?"
Além dessas 4 perguntas que o cliente deverá responder SIM ou NÃO, existe outra validação
que o sistema deve fazer de forma automática que é:
5 - "A renda do cliente é o dobro do valor solicitado?"

Com base nas respostas a essas perguntas, o programa deve emitir uma classificação sobre o
perfil de crédito do cliente, informando se o empréstimo foi aprovado e qual é o valor aprovado.
As regras do negócio são as seguintes:
• Se o sistema receber positivamente a pelo menos duas das cinco perguntas, o cliente
será classificado como " Aprovado com restrições" e o valor aprovado será de 20% do
valor solicitado.
• Se o sistema receber positivamente a três ou quatro das cinco perguntas, o cliente terá a
condição de " Aprovado com desconto" e receberá 60% do valor solicitado.
• Se o cliente responder positivamente a todas as cinco perguntas, ele terá " Aprovação
total ".
• Caso contrário, o cliente será classificado como "Não aprovado".
Crie esse programa e mostre na saída a situação do cliente com o valor a ser emprestado, se a
aprovação for concedida.'''

# Pedir as informações
valor_emprestimo= float(input('Quanto você deseja pegar emprestado? R$'))
renda_mensal=float(input('Qual a sua renda mensal atual? R$'))

print('Seu score é acima de 450 pontos?')
score=input().upper()

print('Você possuí dividas ativas?')
dividas=input().upper()

print('Você é funcionario público?')
funcionario_publico=input().upper()

print('Você concorda em compartilhar seus dados de outros bancos através do open banking?')
dados=input().upper()

# Calcular a pontuação
pontuacao=0

if renda_mensal>=valor_emprestimo*2:
    pontuacao+=1

if score == 'SIM':
    pontuacao+=1

if dividas=='NÃO' or dividas == 'NAO':
    pontuacao+=1

if funcionario_publico == 'SIM':
    pontuacao+=1

if dados == 'SIM':
    pontuacao+=1


# Qual o valor do empréstimo que o cliente pegou

print(f'Sua pontuação foi de {pontuacao}')

if pontuacao == 2:
    print(f'Aprovado com restrições, valor aprovado R${valor_emprestimo*20/100:.2f}')
elif pontuacao == 3 or pontuacao == 4:
    print(f'Aprovado com desconto, valor aprovado R${valor_emprestimo*60/100:.2f}')
elif pontuacao == 5:
    print(f'Aprovação total, valor aprovado R${valor_emprestimo:.2f}')
else:
    print('Empréstimo não aprovado')