# 1. ENTRADAS (valor da hora, horas trabalhadas)
horas_trabalhadas = input('Informe sua quantidade de horas mensais: ')
valor_hora = input('Digite o valor da hora trabalhada: ').replace(",",".")
horas_trabalhadas = float(horas_trabalhadas)
valor_hora = float(valor_hora)

# 2. BRUTO
salario_bruto = valor_hora * horas_trabalhadas

# 3. REGRAS: o if só escolhe o percentual do IR
if salario_bruto <= 900:
  aliquota_ir = 0
elif salario_bruto <= 1500:
  aliquota_ir = 5
elif salario_bruto <= 2500:
  aliquota_ir = 10
else:
  aliquota_ir = 20

# 4. CONTAS: cada conta escrita uma única vez
def calcular_folha(salario_bruto, aliquota_ir):
  valor_ir = salario_bruto * aliquota_ir / 100
  valor_sindicato = salario_bruto * 3 / 100
  valor_fgts = salario_bruto * 11 / 100
  total_descontos = valor_ir + valor_sindicato
  salario_liquido = salario_bruto - total_descontos
  return {
      "ir": valor_ir,
      "sindicato": valor_sindicato,
      "fgts": valor_fgts,
      "total_descontos": total_descontos,
      "salario_liquido": salario_liquido,
  }

folha = calcular_folha(salario_bruto, aliquota_ir)

# 5. IMPRESSÃO
print("=" * 36)
print(f'Valor salário bruto: {salario_bruto}')
print(f'Valor desconto IR: {folha["ir"]}')
print(f'Valor desconto sindicato: {folha["sindicato"]}')
print(f'Valor total de descontos: {folha["total_descontos"]}')
print(f'Valor salário líquido: {folha["salario_liquido"]}')
print(f'Valor de fgts: {folha["fgts"]}')