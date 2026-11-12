# calculadora com while
# o while sempre vai ser true
# primeiro passo, fazer uma forma da pessoa sair, reatribuindo o valor de s
# sair.lower()
# sair = input('Quer sair? [s])
# sair = sair.lower()
# sair = sair.startswitch('s')
while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+-/*): ")
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("um ou ambos os numeros não são validos.")
        continue

    operadores_permitidos = "+-/*"
    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua conta.")

    if operador == "+":
        print(f"{num_1_float} + {num_2_float}=", num_1_float + num_2_float)

    elif operador == "-":
        print(f"{num_1_float} - {num_2_float}=", num_1_float - num_2_float)

    elif operador == "/":
        print(f"{num_1_float} / {num_2_float}=", num_1_float / num_2_float)

    elif operador == "*":
        print(f"{num_1_float} * {num_2_float}=", num_1_float * num_2_float)

    else:
        print("Nunca deveria chegar aqui")

    sair = input("Quer sair? [s] ").lower().startswith("s")
    if sair is True:
        print("Você saiu")
        break
