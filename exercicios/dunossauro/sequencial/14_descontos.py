# Escreva um programa em Python que receba o salário bruto de um funcionário,
# calcule os descontos obrigatórios (IR: 11%, INSS: 8%, Sindicato: 5%)
# e exiba um resumo detalhado contendo o salário bruto, o valor de cada
# desconto e o salário líquido final.


# entrada de salario
salario_bruto = float(input("Digite o seu salario bruto: R$"))

# calculo de descontos
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# calculo de salario liquido
total_descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - total_descontos

# exibindo resultados
print(f"\n--- Resumo do Salário ---")
print(f"+ Salário Bruto: R$ {salario_bruto:.2f}")
print(f"- Imposto de Renda (11%): R$ {imposto_renda:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"= Salário Líquido: R$ {salario_liquido:.2f}")
