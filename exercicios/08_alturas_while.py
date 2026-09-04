#%%
"""
Faça um programa que receba 4 alturas usando laço
de repetição
"""

soma = 0
qtd_entradas = 4

while qtd_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)  # Converte o texto digitado em número decimal
    soma += altura          # Acumula o valor lido na soma total
    qtd_entradas -= 1       # Reduz a contagem para evitar loop infinito

print("Soma das alturas:", soma)