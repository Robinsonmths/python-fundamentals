# media de nota
nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
nota_3 = float(input('Digite a terceira nota do aluno: '))
nota_4 = float(input('Digite a quarta nota do aluno: '))
soma = nota_1 + nota_2 + nota_3 + nota_4
divisao = soma / 4
if divisao < 5:
  print(f'Aluno reprovado{divisao:.1f}')
else:
  print(f'Aluno Aprovado {divisao:.1f}')
