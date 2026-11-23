# identificando vogal
letra = input('Digite uma letra: ').strip()
if letra.lower() in 'aeiou':
  print(f'A letra {letra} é uma vogal')
else:
  print('A letra não é uma vogal')