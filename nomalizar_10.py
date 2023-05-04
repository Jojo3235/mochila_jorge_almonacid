import pandas as pd 
import numpy as np
import sklearn
from sklearn import preprocessing
import os


df = pd.read_csv('pokemon_normalized_2.csv')

num_filas = len(df)

df['valor_10'] = df.apply(lambda x: 10/x.capture_rate + 1.5, axis=1)

# df['proporcion'] = df.apply(lambda x: 1/x.valor_10, axis=1)

df.to_csv('pokemon_normalized_2.csv', index=False)