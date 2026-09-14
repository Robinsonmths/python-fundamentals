#%% 
def juros_compostos(aporte: int, taxa: float, anos: int)-> float :
    """juros_compostos serve para caucular o retorno financeiro a partir de uma aporte.
deve se considerer a taxa de juros e o tempo de aplicação em anos
para o calculo do valor a ser retornado
aporte:
    um numero inteiro que represente o valor em R$
taxa:
    um numero float entre 0 e 1 que represente a taxa de juros
anos:
    um numero inteiro >= 1 que representa o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos



#%%
juros_compostos(1000, 0.13, 4)

# %%
juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)


# %%
