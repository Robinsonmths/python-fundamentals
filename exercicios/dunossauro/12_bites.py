# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
#   Para Megabytes: Gigabytes * 1024
#   Para Kilobytes: Gigabytes * 1024 * 1024
#   Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

informacao = float(input("Digite a quantidade de gigas: "))

# Seus cálculos baseados nas fórmulas do enunciado
megabytes = informacao * 1024
kilobytes = informacao * 1024 * 1024

# Exibindo os dois resultados organizados
print(f"O valor em Megabytes é: {megabytes} MB")
print(f"O valor em Kilobytes é: {kilobytes} KB")
