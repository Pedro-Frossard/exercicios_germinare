import pandas as pd


vendas_df = pd.read_excel(r"C:\Users\pedro\OneDrive\Área de Trabalho\Curso_de_python-Germinare\pandas/Vendas.xlsx")

faturamento_por_loja = vendas_df[["ID Loja","Quantidade", "Valor Final"]].groupby('ID Loja').sum()

faturamento_por_loja = faturamento_por_loja.rename(columns={"Valor Final": "Faturamento"})

print(faturamento_por_loja)