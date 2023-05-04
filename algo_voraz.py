import pandas as pd

df = pd.read_csv('pokemon_normalized_2.csv')

pesos = df['valor_10'].values
valores = df['Total'].values
nombres = df['Name'].values

max_bolsa = 6

lista_pokes = []

peso_acumulado = 0

pokemon_ratios = valores/pesos

indices_ordenados = sorted(range(len(pokemon_ratios)), key=lambda k: -pokemon_ratios[k])

for i in range(max_bolsa):
    idx = indices_ordenados[i]
    if pesos[idx] <= 10 and peso_acumulado + pesos[idx] <= 10:
        selected_poke = nombres[idx]
        max_bolsa -= 1
        peso_acumulado += pesos[idx]
        lista_pokes.append(selected_poke)

print(lista_pokes)
print(peso_acumulado)