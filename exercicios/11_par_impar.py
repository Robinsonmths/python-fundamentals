# a função tem uma e apenas uma regra
def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input ("Entre com um numero: "))# não e interessante inserir nada dentro da função
print(par_impar(numero))
