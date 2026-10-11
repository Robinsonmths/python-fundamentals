"""
Repeticoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:  # o continue pula a condição
        print("não mostra o 6")
        continue

    if contador >= 10 and contador <= 27:
        print("vou pular uma parte da sequencia")
        continue

    print(contador)
    if contador == 40:  # quebra o laço
        break
print("Acabou")
