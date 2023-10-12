tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo da aula em MB: "))
velocidade_conexao_mbps = float(input("Digite a velocidade da conexão em Mbps: "))

tamanho_arquivo_mbps = tamanho_arquivo_mb * 8
tempo_estimado_segundos = tamanho_arquivo_mbps / velocidade_conexao_mbps
tempo_estimado_ate_60_seg = tempo_estimado_segundos <= 60

print(f"Tempo estimado de download: {tempo_estimado_segundos:.2f} segundos")
print(f"Download é considerado rápido: {tempo_estimado_ate_60_seg}")
