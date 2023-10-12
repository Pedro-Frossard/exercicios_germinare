# Pedir informação ao usuário
string = str(input('Digite uma palavra/frase: '))

# Fazer a função que conta as vogais 
def contar_vogais(string):
    string.lower()
    total_de_vogais = string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u')
    return total_de_vogais

# Mostrar o resultado
print(f'A sua palavra/frase tem {contar_vogais(string)} vogais.')
    