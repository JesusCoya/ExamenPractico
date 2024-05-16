import pandas as pd
from sklearn.preprocessing import RobustScaler

# Cargar el conjunto de datos desde el archivo CSV
try:
    data = pd.read_csv("Twitch_game_data.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    try:
        data = pd.read_csv("Twitch_game_data.csv", encoding="latin1")
    except UnicodeDecodeError:
        data = pd.read_csv("Twitch_game_data.csv", encoding="iso-8859-1")

data = data.iloc[:, 3:]

# Mostrar el DataFrame original
print("DataFrame original:")
print(data.head())

# Seleccionar las columnas a escalar (todas excepto la columna 'Outcome')
columnas_a_escalar = data.columns[:-1]

# Crear una instancia de RobustScaler
scaler = RobustScaler()

# Escalar los datos
data[columnas_a_escalar] = scaler.fit_transform(data[columnas_a_escalar])

# Mostrar el DataFrame preprocesado
print("\nDataFrame después de escalar con RobustScaler:")
print(data.head())
