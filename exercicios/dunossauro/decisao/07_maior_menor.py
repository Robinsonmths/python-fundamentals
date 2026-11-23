# maior e menor numero
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

if a > b and a > c:
  print(f'O numero {a} é maior')

if b > a and b > c:
  print(f'O numero {b} é maior')

if c > a and c > b:
  print(f'O numero {c} é maior')

if a < b and a < c:
  print(f'O numero {a} é menor')

if b < a and b < c:
  print(f'O numero {b} é menor')

if c < a and c < b:
  print(f'O numero {c} é menor')