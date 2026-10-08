#%%
dados_matheus = [26,1,'casado', 'analista de dados']
dados_matheus

#%%
dados_matheus.append('3215651,52')
dados_matheus

#%%
tupla_matheus = (26,1,'casado', 'analista de dados',['oculos','relogio'])
# tupla_matheus = 26,1,'casado', 'analista de dados'
print (type(tupla_matheus))
print (tupla_matheus)
# a tupla e imutavel

# %%
#listas dentro de tuplas podem ser alteradas
tupla_matheus[4].append('celular')
print(tupla_matheus)