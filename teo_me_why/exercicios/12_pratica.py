"""
Peça para o usuário digitar o ano em que nasceu.
Peça para o usuário digitar o ano atual.
Calcule a idade da pessoa.
Exiba uma mensagem dizendo: "Você tem X anos." (ou "Você fará X anos este ano.").
"""

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite o ano que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
print(f"Seu nome é: {nome} e sua idade é:{idade}")