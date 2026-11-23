# qual numero e negativo ?
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
numero_1 = float(numero_1)
numero_2 = float(numero_2)
if numero_1 < 0:
  print(f'o número {numero_1} é negativo')
elif numero_2 < 0:
  print(f'o número {numero_2} é negativo')
else:
  print('Nenhum número é negativo')