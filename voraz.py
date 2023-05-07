import pandas as pd

def mochila_pokemon(df, limite_mochila, limite_peso):
    # Ordenar por el ratio de valor para peso
    df = df.sort_values(by=['valor_10'], ascending=False)

    pokes = []
    peso_actual = 0
    beneficio_total = 0

    # Añadir pokémon a la mochila mientras se pueda
    for _, row in df.iterrows():
        if (peso_actual + row['valor_10']) <= limite_peso and len(pokes) < limite_mochila:
            pokes.append(row['Name'])
            peso_actual += row['valor_10']
            beneficio_total += row['Total']
    
    # Si no se llenó la mochila, buscar equipo de 6 pokémon
    if len(pokes) < limite_mochila:
        df2 = df[~df['Name'].isin(pokes)]
        df2 = df2.sort_values(by=['valor_10'], ascending=False)

        for _, row in df2.iterrows():
            if (peso_actual + row['valor_10']) <= limite_peso and len(pokes) < limite_mochila:
                pokes.append(row['Name'])
                peso_actual += row['valor_10']
                beneficio_total += row['Total']
    
    return pokes, beneficio_total, peso_actual


def main():
    # Leer el archivo CSV
    df = pd.read_csv('pokemon.csv')

    # Parámetros de la mochila
    limite_mochila = 6
    limite_peso = 10

    # Resolver la mochila
    pokes, beneficio_total, peso_total = mochila_pokemon(df, limite_mochila, limite_peso)

    # Imprimir resultados
    print("Pokémon en la mochila:")
    print(pokes)
    print("Beneficio total:", beneficio_total)
    print("Peso total:", peso_total)
