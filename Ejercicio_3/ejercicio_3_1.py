import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Cargar el dataset CSV
try:
    data = pd.read_csv("Twitch_game_data.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    try:
        data = pd.read_csv("Twitch_game_data.csv", encoding="latin1")
    except UnicodeDecodeError:
        data = pd.read_csv("Twitch_game_data.csv", encoding="iso-8859-1")

# Eliminar las primeras dos columnas
# data = data.iloc[:, 1:]

# Identificar columnas categóricas
columnas_categoricas = [
    "Game",
    # "Otra_columna_categorica",
]

# Aplicar OneHotEncoder a las columnas categóricas
encoder = OneHotEncoder(handle_unknown="ignore")
datos_onehot = encoder.fit_transform(data[columnas_categoricas])

# Convertir el resultado a un DataFrame
datos_onehot_df = pd.DataFrame(
    datos_onehot.toarray(), columns=encoder.get_feature_names_out(columnas_categoricas)
)

# Combinar el DataFrame original con el DataFrame codificado
data_final = pd.concat(
    [data.drop(columnas_categoricas, axis=1), datos_onehot_df], axis=1
)

# Imprimir el DataFrame final
print(data_final)
