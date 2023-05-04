import pandas as pd
import numpy as np
import os


df = pd.read_csv("pokemon.csv")

df2 = pd.read_csv("capture_rate.csv")

df_3 = pd.concat([df, df2], axis=1)

df_3.to_csv("pokemon_rates.csv", index=False)