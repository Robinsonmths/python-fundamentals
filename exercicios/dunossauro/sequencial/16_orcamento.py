# Crie um programa de cálculo de orçamento para uma loja de tintas.
# O usuário deve informar a área em m². Considere que 1L cobre 6m²,
# adicione 10% de folga ao total de tinta, e utilize os seguintes insumos:
# - Lata de 18L: R$ 80,00
# - Galão de 3,6L: R$ 25,00
#
# O programa precisa retornar a quantidade de itens e o preço total para:
# - Cenário A: Apenas latas de 18L.
# - Cenário B: Apenas galões de 3,6L.
# - Cenário C: Mistura otimizada entre latas e galões para menor desperdício.

# input do sistema
medicao = float(input("Digite os metros quadrados: "))

# constantes
TAMANHO_LATA = 18
VL_LATA = 80.00
TAMANHO_GALAO = 3.6
VL_GALAO = 25.00
RENDIMENTO = 6

# calculos
LITROS_BRUTOS = medicao / RENDIMENTO
VOLUME_TOTAL = LITROS_BRUTOS * 1.10

# descobrindo latas
latas_necessarias = int(VOLUME_TOTAL // TAMANHO_LATA)
if VOLUME_TOTAL % TAMANHO_LATA > 0:
    latas_necessarias += 1
preco_latas = latas_necessarias * VL_LATA

# descobrindo galão
galoes_necessarios = int(VOLUME_TOTAL // TAMANHO_GALAO)
if VOLUME_TOTAL % TAMANHO_GALAO > 0:
    galoes_necessarios += 1
preco_latas = galoes_necessarios * VL_GALAO

# qtd final
latas_mistura = int(VOLUME_TOTAL // TAMANHO_LATA)
litros_restantes = VOLUME_TOTAL % TAMANHO_LATA

galoes_mistura = int(litros_restantes // TAMANHO_GALAO)
if litros_restantes % TAMANHO_GALAO > 0:
    galoes_mistura += 1

preco_mistura = (latas_mistura * VL_LATA) + (galoes_mistura * VL_GALAO)
