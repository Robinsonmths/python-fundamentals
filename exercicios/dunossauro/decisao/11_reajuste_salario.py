# reajuste de salario
valor = float(input('Digite o salário: '))

if valor <= 280:
    percentual = 20
elif valor < 700:
    percentual = 15
elif valor < 1500:
    percentual = 10
else:
    percentual = 5

aumento = valor * percentual / 100
novo_salario = valor + aumento

print(f'Salário antigo: R$ {valor:.2f}')
print(f'Aumento de {percentual}%: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')