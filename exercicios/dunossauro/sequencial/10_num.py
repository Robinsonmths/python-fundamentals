# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    O produto do dobro do primeiro com metade do segundo .
#    A soma do triplo do primeiro com o terceiro.
#    O terceiro elevado ao cubo.

prim_num = int(input("Digite primeiro numero"))
seg_num = int(input("Digite segundo numero"))
ter_num = int(input("Digite terceciro numero"))
resultado1 = (prim_num * 2) * (seg_num / 2)
resultado2 = (prim_num * 3) + ter_num
resultado3 = ter_num**3

print(f"resultados {resultado1} {resultado2} {resultado3}")
