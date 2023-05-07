import pandas as pd 
import numpy as np
import sklearn
from sklearn import preprocessing
import os


df = pd.read_csv('pokemon.csv')

# num_filas = len(df)

# #crear columna de valor_10 total**2/(300-capture_rate)
df["peso"] = df["Total"]**2/(800-df["capture_rate"])**2

# # suma de los valores de la columna peso

suma_pesos = df["peso"].sum()

df["valor_10"] = df["peso"]/suma_pesos*1000 -0.4

# # df.drop(columns=['peso'], inplace=True)
# # print(suma_pesos)
df.to_csv('pokemon.csv', index=False)