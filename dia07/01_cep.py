#%%
import requests #requisições web
import json #trata json para arquivos
from tqdm import tqdm
import pandas as pd
ceps = [
    "74933640",
    "74150130", 
    "74915520"
]

url = "https://viacep.com.br/ws/{cep}/json/"



dados = [] # passando pela lista de ceps caso o retorno seja 200
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
dados
# %%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

