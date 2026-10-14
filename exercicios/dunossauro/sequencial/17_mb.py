# Requisito do Sistema - Calculadora de Tempo de Download:
# Desenvolva um programa que estime o tempo necessário para baixar um arquivo
# da internet com base no tamanho do arquivo e na velocidade da conexão.
#
# O sistema deve solicitar ao usuário:
# 1. O tamanho do arquivo para download (em Megabytes - MB).
# 2. A velocidade do link de internet (em Megabits por segundo - Mbps).
#
# Regras de Negócio e Conversão:
# - A velocidade da internet é dada em Megabits (Mb), mas o arquivo está em
#   Megabytes (MB). Lembre-se de que 1 Byte equivale a 8 bits (1 MB = 8 Mb).
# - O tempo final de download deve ser convertido e exibido em minutos.
#
# O programa deve informar ao usuário o tempo aproximado de download.

# 1. Entrada de dados
tamanho_mb = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (em Mbps): "))

# 2. PROCESSAMENTO E CÁLCULOS
# Transformando Megabytes em Megabits (1 MB = 8 Mb)
tamanho_megabits = tamanho_mb * 8

# Calculando o tempo em segundos e convertendo para minutos
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

# 3. EXIBIÇÃO DOS RESULTADOS
print(f"\n--- Relatório de Download ---")
print(f"Tamanho do arquivo: {tamanho_mb} MB")
print(f"Velocidade da conexão: {velocidade_mbps} Mbps")
print(f"Tempo aproximado: {tempo_minutos:.2f} minutos")
