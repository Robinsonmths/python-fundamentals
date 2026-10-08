"""
Repeticoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
break -> dentro do while, sai do while mais proximo
"""

condicao = True

while condicao:
    nome = input("Qual seu nome? ")
    print(f"Seu nome é {nome}")
    if nome == "sair":
        break

print("acabou")
