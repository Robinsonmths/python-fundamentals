"""
Faça um programa que receba uma quantidade de valores indefinida
valores devem corresponder a "saldo em conta"
Mas se o usuário apertar "enter", sem digitar valor
o programa exibe a soma dos valores
digitados anteriormente
"""

saldo_total = 0

while True:
    saldo= input ("Entre com o saldo: ")

    if saldo == '':
        break #sai do laço mais proximo

    saldo_total += float(saldo)

print("Saldo total", saldo_total)