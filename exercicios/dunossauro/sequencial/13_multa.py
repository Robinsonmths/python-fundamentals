# João, um pescador, comprou um microcomputador
# para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que
# o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00
# por quilo excedente.
# João precisa que você faça um programa que
# leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

kg_pescados = float(input("Digite a quantidade de kg, pescado: "))
limite = 50
calculo = kg_pescados - limite
multa = calculo * 4
if kg_pescados > limite:
    print(f"foi excedido a quantidade o valor ser pago é {multa}")
else:
    print("Sem multas no momento")
