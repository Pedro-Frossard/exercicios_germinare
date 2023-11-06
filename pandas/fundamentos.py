import pandas as pd



# Dataframe == tabela
# criar dataframe --> pd.DataFrame()
vendas = {'data': ['16/02/2021', '04/11/20230'],
          'valor': [500,300],
          'produtos': ['feijão','arroz'],
          'quantidade': [50,70]
        }
#vendas_df = pd.DataFrame(vendas) #criar DataFrame a partir de um dicionario

#print(vendas_df)

'''Outro metodo de fazer um dataframe, importando de uma base de dados'''

vendas_exel_df = pd.read_excel(r"C:\Users\pedro\OneDrive\Área de Trabalho\Curso_de_python-Germinare\pandas/Vendas.xlsx")


#print(vendas_exel_df)
# ou
#print(vendas_exel_df.head(5)) #--> 50 primeiras linhas
#print(vendas_exel_df.shape) --> ve quantas linhas e colunas tem, mais rapido que um print
#print(vendas_exel_df.describe()) # Analise de dados completa, count = numero de valores, mean = média dos valores númericos, std = média dos valores que saem da mean e etc

'''Editar tabela e pegar valores'''

#Pegar colunas especificas
        #produtos = vendas_exel_df['Produto']
        #print(produtos)

#Pegar mais de uma coluna
        #proodutos_valorFinal = vendas_exel_df[['Produto','Valor Final']]
        #print(proodutos_valorFinal)

#Pegar linha especifica com .loc
        #print(vendas_exel_df.loc[1])# igual manipulação de str
        #print(vendas_exel_df[20:1:-1])

#Pegar valores especificos com .loc
        #print(vendas_exel_df.loc[(vendas_exel_df['Valor Final'] > 500)  & (vendas_exel_df['ID Loja'] == 'Shopping Ibirapuera')]) # Pego valores que tem seu valor final maior que 500 reais e ID loja o shopping ibirapuera, não esquecer do E comercial (&) e dos parenteses
        # Se quiser fazer uma validação como or use | em vez de &
        # Se eu quiser filtrar linhas e colunas ao mesmo tempo, loc tem como padrão loc[linhas, colunas]
        #print(vendas_exel_df.loc[(vendas_exel_df['Valor Final'] > 500)  & (vendas_exel_df['ID Loja'] == 'Shopping Ibirapuera'), ["ID Loja","Quantidade","Valor Final"]])
        # Se eu quiser pegar apenas 1 valor, lembre .loc[linha, coluna]
            #print(vendas_exel_df.loc[1,'Produto'])

# Adicionar coluna
        # A partir de uma coluna que ja existe
vendas_exel_df['Comissão'] = vendas_exel_df['Valor Final'] * 0.05

        # Criar uma coluna com valor padrão
vendas_exel_df.loc[:, 'Imposto'] = 0  # Ainda estão decidindo o valor do imposto/: no loc é igual a tudo, então neste caso eu seleciono todas as linhas


# Adicionar linhas, neste caso de outro documento exel
vendas_Dez= pd.read_excel(r"C:\Users\pedro\OneDrive\Área de Trabalho\Curso_de_python-Germinare\pandas/Vendas - Dez.xlsx")
vendas_exel_df = vendas_exel_df._append(vendas_Dez)

# Excluir linhas e colunas
#Excluir coluna --> 
    #vendas_exel_df = vendas_exel_df.drop(['Quantidade'], axis=1)
    # Excluir linha --> vendas_exel_df = vendas_exel_df.drop([indice da linha, axis=0])
    # axis determina o que voce quer excluir, linha ou coluna no caso do axis 0 é para linha e 1 para coluna

# Excluir valores vazios
    # vendas_exel_df = vendas_exel_df.dropna(how='all', axis=1) # Aqui eu mando ele excluir as colunas (axis=1) que tem todos os valores vazios
    # vendas_exel_df = vendas_exel_df.dropna(how='any', axis=1) # Aqui eu mando ele excluir as colunas (axis=1) que tenha qualquer valor vazio

# Preencher valores vazios
    #vendas_exel_df["Comissão"] = vendas_exel_df['Comissão'].fillna(vendas_exel_df['Valor Final']*0.05)
    #vendas_exel_df["Imposto"] = vendas_exel_df['Imposto'].fillna(0)

    # Preencher com o ultimo valor --> vendas_exel_df = vendas_exel_df.ffill()

# Calcular indicadores
    #vendas_por_produto = vendas_exel_df['Produto'].value_counts() # Retorna a quantidade de produtos de cada produto do maior para o menor

    #total_vendido = vendas_exel_df[['Produto', 'Valor Final']].groupby('Produto').sum() # Primeiro eu seleciono as colunas que eu quero agrupar depois eu agrupo somando, com o metodo sum()


    # total_vendido.rename(columns={'Valor Final': 'Faturamento'}, inplace=True) # Aqui eu apenas renomeei a coluna que estava "Valor Final" por "Faturamento" que é bem mais lógico

# Mesclar Tabela
gerentes_df = pd.read_excel(r"C:\Users\pedro\OneDrive\Área de Trabalho\Curso_de_python-Germinare\pandas/Gerentes.xlsx")

#vendas_exel_df = vendas_exel_df.merge(gerentes_df)

#print(vendas_exel_df)


