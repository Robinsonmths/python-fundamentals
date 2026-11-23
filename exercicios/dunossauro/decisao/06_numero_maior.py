# apresentando o maior numero
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o terceiro numero: '))

if numero_1 > numero_2 and numero_1 > numero_3:
  print(f'O numero {numero_1} é maior')

if numero_2 > numero_1 and numero_2 > numero_3:
  print(f'O numero {numero_2} é maior')

if numero_3 > numero_2 and numero_3 > numero_1:
  print(f'O numero {numero_3} é maior')