#%%
import requests         #requisições web
import json             #trata json para arquivos
from tqdm import tqdm   
import pandas as pd

url = "https://api.opendota.com/api/heroes"

resp = requests.get(url)
df = pd.DataFrame(resp.json())
df.to_csv("heroes_dota.csv", sep=";")