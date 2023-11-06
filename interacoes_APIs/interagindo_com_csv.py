import csv
import os


caminho_absoluto = os.path.abspath('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Curso_de_python-Germinare\\interacoes_APIs\\b.txt')


with open(caminho_absoluto,'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter = ',')

    for linha in arquivo_csv:
        print(linha)