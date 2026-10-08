"""
Defina um usuário e senha padrão no seu código 
(ex: usuario_salvo = "admin" e senha_salva = "1234").
Peça para o usuário digitar o nome de usuário.
Peça para o usuário digitar a senha.
Se o usuário E a senha digitados forem iguais aos salvos, exiba:
 "Acesso concedido! Bem-vindo."
Caso contrário, exiba: "Usuário ou senha incorretos.
 Acesso negado."
"""

usuario_salvo = "system"
senha_salva = 12345
usuario = str(input("Entre com seu usuário: "))
senha = int(input("Entre com sua senha: "))
if usuario == usuario_salvo and senha == senha_salva:
    print("Acesso liberado")
else:
    print ("Acesso negado")