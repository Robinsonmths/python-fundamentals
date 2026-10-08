"""
Peça para o usuário digitar o nome do produto.
Peça o preço original do produto.
Peça a porcentagem de desconto (exemplo: 10 para 10%).
Calcule o valor do desconto e o preço final do produto.
Exiba o nome do produto, o valor economizado e o preço final.
"""

produto = str(input("Digite o nome do produto: "))
prec_original = float(input("Digite o valor original do produto: "))
percent_desc = float(input ("Digite o percentual de desconto: "))
valor_desconto = prec_original * (percent_desc / 100)
print (f"O seu produto é {produto}, o preço original é: {prec_original}, aplicando o desconto de {percent_desc}, o valor do desconto é {valor_desconto}")