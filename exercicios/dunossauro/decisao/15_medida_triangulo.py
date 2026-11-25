"""
Triângulo inválido exemplo:
Lado A = 2
Lado B = 3
Lado C = 8
A soma dos dois menores é 2 + 3 = 5, que é menor que 8.
Entrada inválida: o usuário deixa vazio ou digita letras.
"""
#inputs
a = float(input('Digite o valor da lado 1: '))
b = float(input('Digite o valor da lado 2: '))
c = float(input('Digite o valor da lado 3: '))

#soma
valor_1 = a + b
valor_2 = a + c
valor_3 = b + c

#comparacao
if valor_1 > c and valor_2 > b and valor_3 > a:
  if a == b and a == c:
    print('O triângulo e equilátero')
  elif a == b or a == c or b == c:
    print('O triângulo e isoceles')
  else:
    print('O triângulo e escaleno')
else:
  print('Triângulo inválido.')
