# saudação personalizada
turno = input('Digite seu turno: ')
turno = turno.strip().lower()

if turno == 'm':
  print(f'Bom dia!')

elif turno == 'v':
  print(f'Boa tarde!')

elif turno == 'n':
  print(f'Boa noute!')

else:
  print('Valor inválido:')