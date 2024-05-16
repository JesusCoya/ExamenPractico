import pandas as pd
from sklearn.impute import SimpleImputer

# Cargar el conjunto de datos desde un archivo CSV
try:
    data = pd.read_csv("Twitch_game_data.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    try:
        data = pd.read_csv("Twitch_game_data.csv", encoding="latin1")
    except UnicodeDecodeError:
        data = pd.read_csv("Twitch_game_data.csv", encoding="iso-8859-1")

data = data.iloc[:, 3:]
# Mostrar el DataFrame antes de la imputación
print("DataFrame original:")
print(data)

# Identificar las columnas que tienen ceros
columnas_con_ceros = data.columns[data.eq(0).any()]

# Reemplazar los ceros con NaN en las columnas identificadas
data[columnas_con_ceros] = data[columnas_con_ceros].replace(0, float("nan"))

# Crear una instancia de SimpleImputer con la estrategia de imputación como 'mean'
imputer = SimpleImputer(strategy="mean")

# Imputar los valores faltantes con la media en las columnas identificadas
data[columnas_con_ceros] = imputer.fit_transform(data[columnas_con_ceros])

# Mostrar el DataFrame preprocesado por terminal
print("\nDataFrame después de la imputación:")
print(data)
