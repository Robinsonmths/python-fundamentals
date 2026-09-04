#%%
# Dicionário: estrutura que armazena dados em pares de 'chave: valor'
dados_matheus = {
    'nome':'matheus',
    'sobrenome':'santos',
    'filhos':True,
    'formacao':['analise de dados', 'datascience']
}
print(dados_matheus)

#%%
dados_matheus['formacao']
# %%
dados_matheus['formacao'][-1]
# %%
dados_matheus['estado_civil'] =  'casado'
print(dados_matheus)

#%%
print('chaves: ',dados_matheus.keys())
print('valores: ',dados_matheus.values())
print('itens: ',dados_matheus.items())
# %%
for i in dados_matheus:
    print(i)
# %%
for i in dados_matheus:
    print(i, "-> ", dados_matheus[i])
# %%
for item in dados_matheus.items():
    print(item)

#%%
for chave, valor in dados_matheus.items():
    print(chave, "-> ",valor)
# %%
