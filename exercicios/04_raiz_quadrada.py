"""
faça um programa que receba um numero inteiro e calcule a raiz quadrada desse numero.
"""

numero = int(input("Digite um numero inteiro: "))
raiz_quadrada = numero ** 0.5
raiz_quadrada = round(raiz_quadrada, 2)
print("A raiz quadrada de", numero, "é", raiz_quadrada)