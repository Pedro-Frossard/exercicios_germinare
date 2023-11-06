print('Comparação de consumo de combustível\n\n')
veiculos = []
for automovel in range(1,6):
    print(f'Veiculo {automovel}')
    nome_veiculo = input('Nome: ')
    km_por_litro = float(input('Km por litro: '))
    veiculos.append([nome_veiculo,km_por_litro])

print('Relatorio final:')
for numero,veiculo in enumerate(veiculos):
    print(f'{numero+1} - {veiculo[0].lower():<10}-{veiculo[1]:>6} -{1000/veiculo[1]:>7.1f} litros - R$ {1000/veiculo[1]*2.25:.2f}')
    mais_economico = veiculos[0][1]
    nome_mais_economico = veiculos[0][0]
    if veiculos[numero][1] > mais_economico:
        mais_economico = veiculos[numero][1]
        nome_mais_economico = veiculos[numero][0]
print(f'O veículo mais economico é o {nome_mais_economico} gastando 1 litro a cada {mais_economico}km')

