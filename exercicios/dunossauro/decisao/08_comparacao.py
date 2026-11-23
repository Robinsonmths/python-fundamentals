# comparação de valor
produto_a = float(input('Digite o valor do produto A:'))
produto_b = float(input('Digite o valor do produto B:'))
produto_c = float(input('Digite o valor do produto C:'))

valor = produto_a

if produto_b < valor:
  valor = produto_b

if produto_c < valor:
  valor = produto_c

print(f'O Menor valor é {valor}')