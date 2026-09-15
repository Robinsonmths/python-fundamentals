#%%
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto = preco * kwargs[i]

    return imposto

impostos_gerais = { 
    "municipa"  : 0.01, 
    "estadual"  : 0.005, 
    "nascional" : 0.001
}

calc_imposto(100, 0.03, **impostos_gerais )




#%%
# 1. IMPORTS DE BIBLIOTECAS (se houver)
import os


# 2. CONSTANTES / CONFIGURAÇÕES FIXAS
# Dicionários de taxas e valores padrão geralmente ficam no topo como constantes
TAXAS_IMPOSTOS_PADRAO = {
    "municipal": 0.01,
    "estadual": 0.005,
    "nacional": 0.001
}
TAXA_BASE_PADRAO = 0.03


# 3. DEFINIÇÃO DAS FUNÇÕES
# As funções precisam ser declaradas ANTES de serem chamadas no código
def calc_imposto(preco: float, tx_base: float, **kwargs) -> float:
    imposto_total = preco * tx_base

    for nome_imposto, taxa in kwargs.items():
        imposto_total += preco * taxa

    return imposto_total


# 4. EXECUÇÃO PRINCIPAL / FLUXO DE DADOS
# Aqui você define as variáveis dinâmicas do usuário/sistema e chama as funções
preco_produto = 150.00

# Chamada usando as constantes configuradas acima
imposto_final = calc_imposto(
    preco_produto, 
    TAXA_BASE_PADRAO, 
    **TAXAS_IMPOSTOS_PADRAO
)

print(f"Preço: R$ {preco_produto:.2f}")
print(f"Imposto Total: R$ {imposto_final:.2f}")