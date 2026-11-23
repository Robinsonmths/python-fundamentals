# cálculo de uma folha de pagamento
horas_trabalhadas = input('Informe sua quantidade de horas mensais: ')
valor_hora = input('Digite o valor da hora trabalhada: ').replace(",",".")
horas_trabalhadas = float(horas_trabalhadas)
valor_hora = float(valor_hora)

# calculo de salário
salario_bruto = valor_hora * horas_trabalhadas
print(salario_bruto)

# faixas
faixa_1 = salario_bruto * 5 / 100
faixa_2 = salario_bruto * 10 / 100
faixa_3 = salario_bruto * 20 / 100
salario_liquido_1 = salario_bruto - faixa_1
salario_liquido_2 = salario_bruto - faixa_2
salario_liquido_3 = salario_bruto - faixa_3

# regras
if salario_bruto <= 900:
  print(f'livre de descontos {salario_bruto}')

elif salario_bruto <= 1500:
  print(f'Salário com 5% de desconto R${faixa_1} valor do salario é {salario_liquido_1}')

elif salario_bruto <= 2500:
  print(f'Salário sofre 10% de desconto R${faixa_2} valor do salario é {salario_liquido_2}')

elif salario_bruto >= 2500:
  print(f'Salário sofre 20% de desconto R${faixa_3} valor do salario é {salario_liquido_3}')