#%%

txt = """Esse é apenas um teste para saber como se escreve um arquivo \n
    se mudar no campo de texto ele subscreve oque foi salvo anteriormente \n
    mudando o parametro do mode ele muda o comportamento do texto
    """
nome_arquivo = "historia_02.txt"
with open (nome_arquivo, mode="w") as open_file:
    open_file.write(txt)