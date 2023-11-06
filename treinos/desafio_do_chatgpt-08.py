# Código com erros menos perceptíveis

def selecao_ordenada(lista):
    n = len(lista)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
                
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        
# Lista de números a serem ordenados
numeros = [64, 25, 12, 22, 11]

# Chamar a função de ordenação
selecao_ordenada(numeros)

# Exibir a lista ordenada
print("Lista ordenada:", numeros)
