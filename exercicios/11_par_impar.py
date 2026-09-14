#%%
def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input ("Entre com um numero: "))
par_impar(numero)
