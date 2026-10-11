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
conta = 0


if opcao == "1":
    conta = 1.5

elif opcao == "2":
    conta = 2.5 

if conta == 0:
    print ("Entre com a merda da opção correta")

else:
    print("Sua conta é: R$",conta)