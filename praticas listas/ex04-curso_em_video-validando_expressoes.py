expressao = input('Digite uma expressão numerica: ')

if expressao.count('(') == 0 and expressao.count(')') == 0 or expressao.count('(') == expressao.count(')'):
    print(f'A expressão numerica "{expressao}" está valida em termo de parenteses')
else:
    print(f'A expressão numerica "{expressao}" não tem parenteses validos')