# Requisito do Sistema - Loja de Tintas:
# Desenvolva um programa que calcule o custo e a quantidade de latas de tinta
# necessárias para pintar uma determinada área residencial ou comercial.
#
# Parâmetros de cálculo:
# - Rendimento da tinta: 1 litro para cada 3 metros quadrados.
# - Embalagem: Lata de 18 litros.
# - Custo por lata: R$ 80,00.
#
# O programa deve solicitar a área em metros quadrados (m²) e retornar:
# 1. A quantidade total de latas de tinta a serem compradas.
# 2. O preço total da compra.

# input do sistema
medicao = float(input("Digite os metros quadrados: "))

# constantes
TAMANHO_LATA = 18
RENDIMENTO_LITRO = 3
VALOR_LATA = 80.00

# calculos
litros_necessarios = medicao / RENDIMENTO_LITRO

# Descobrindo quantas latas
latas_necessarias = int(litros_necessarios // TAMANHO_LATA)
if litros_necessarios % TAMANHO_LATA > 0:
    latas_necessarias += 1

preco_total = latas_necessarias * VALOR_LATA

# Exibindo os resultados
print(f"\n--- Orçamento da Pintura ---")
print(f"Área a ser pintada: {medicao} m²")
print(f"Latas necessárias: {latas_necessarias} lata(s)")
print(f"Preço total: R$ {preco_total:.2f}")
