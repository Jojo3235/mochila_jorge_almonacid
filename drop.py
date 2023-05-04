import pandas as pd

df = pd.read_csv('pokemon_normalized_2.csv')

df = df.drop(['proporcion'], axis=1)

df.to_csv('pokemon_normalized_2.csv', index=False)