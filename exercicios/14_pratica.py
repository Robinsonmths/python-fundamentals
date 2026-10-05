"""
Peça ao usuário para digitar a nota de um aluno (de 0 a 10).
Se a nota for maior ou igual a 7, exiba: "Aprovado! Parabéns!"
Se a nota for maior ou igual a 5 e menor que 7, exiba: "Recuperação."
Se a nota for menor que 5, exiba: "Reprovado."
"""

nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
    print("Aprovado, Parabéns!")
elif nota >= 5:
    print("Recuperação. ")
else:
    print ("Reprovado")