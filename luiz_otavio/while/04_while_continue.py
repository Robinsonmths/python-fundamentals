"""
Repeticoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("falta o 6")
        continue

    if contador >= 10 and contador <= 27:
        print(f"não vou mostrar o {contador}")
        continue

    print(contador)

    if contador == 40:
        break


print("Acabou")
