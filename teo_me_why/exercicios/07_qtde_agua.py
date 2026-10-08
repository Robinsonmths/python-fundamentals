"""
Faça um programa que vende garrafa de agua:
agua natural R$1,50
agua com gas R$2,50
"""

texto = """
Escolha a sua água para comprar
(1) Agua natural 
(2) Agua com gás
"""
opcao = input (texto)
valor_item = 0


if opcao == "1":
    valor_item = 1.5

elif opcao == "2":
    valor_item = 2.5 

if valor_item == 0:
    print ("Entre com a merda da opção correta")



else:
    qtde = int(input("Quantas garrafas ? "))
    valor_total = valor_item * qtde
    print("Sua conta deu: R$ ",valor_total)
