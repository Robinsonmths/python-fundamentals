qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1

print("Acabou")
# Loop externo: controla o número da tabuada (1, 2 e 3)
# multiplicador = 1

# while multiplicador <= 3:
#     print(f"\n--- Tabuada do {multiplicador} ---")

#     # Loop interno: roda de 1 a 3 para cada número do loop externo
#     numero = 1
#     while numero <= 3:
#         resultado = multiplicador * numero
#         print(f"{multiplicador} x {numero} = {resultado}")
#         numero += 1

#     multiplicador += 1

# print("\nFim da tabuada!")
