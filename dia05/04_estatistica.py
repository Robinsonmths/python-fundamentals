#%%
def soma (a: float, b: float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media (a: float, b: float, *args)->float:
    # Opção 1: Usando a sua função soma() já definida
    return soma(a, b, *args) / (len(args) + 2)

    # Opção 2: Se quisesse usar sum() nativo diretamente:
    # return sum([a, b] + list(args)) / (len(args) + 2)

#%%
a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
print ("Media: ", media (a,b,c))