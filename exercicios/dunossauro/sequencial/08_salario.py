# Faça um programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido
# mês.

hora_salario = float(input("Digite seu valor de hora: "))
horas_diarias = 8
qtd_dias = int(input("digite a quantidade de dias trabalhados"))
calculo = hora_salario * horas_diarias * qtd_dias
print(f"Seu salario é {calculo}")
