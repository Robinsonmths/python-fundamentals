"""
Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
    Maçã: R$ 1,50       Goiaba: R$ 2,15
    Pera: R$ 1,25       Banana: R$ 2,75
    Laranja: R$ 0,65    Uva: R$ 1,90
    Abacaxi: R$ 3,20    Limão: R$ 1,25
    Jaca: R$ 5,80
"""

frutas = {
    "maçã": 1.50,
    "goiaba": 2.15,
    "pera": 1.25,
    "banana": 2.75,
    "laranja": 0.65,
    "uva": 1.90,
    "abacaxi": 3.20,
    "limão": 1.25,
    "jaca": 5.80
}
pedido = input('Digite o nome da fruta: ')
if pedido in frutas:
    print(f'O preço da fruta {pedido} e R$ {frutas[pedido]}')