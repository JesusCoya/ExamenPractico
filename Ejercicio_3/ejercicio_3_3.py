import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar el dataset CSV
# Cargar el dataset CSV
try:
    data = pd.read_csv("Twitch_game_data.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    try:
        data = pd.read_csv("Twitch_game_data.csv", encoding="latin1")
    except UnicodeDecodeError:
        data = pd.read_csv("Twitch_game_data.csv", encoding="iso-8859-1")

data = data.iloc[:, 3:]
# Seleccionar las columnas a escalar
columnas_a_escalar = ["Peak_viewers"]  # Puedes ajustar esto según tus datos

# Crear instancia de StandardScaler
scaler = StandardScaler()

# Escalar las columnas seleccionadas
data[columnas_a_escalar] = scaler.fit_transform(data[columnas_a_escalar])

# Mostrar el DataFrame preprocesado por terminal
print(data)
