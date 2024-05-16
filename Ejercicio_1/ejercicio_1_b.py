import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("./Twitch_game_data.csv", encoding="utf-8")
except UnicodeDecodeError:
    try:
        df = pd.read_csv("./Twitch_game_data.csv", encoding="latin1")
    except UnicodeDecodeError:
        df = pd.read_csv("./Twitch_game_data.csv", encoding="iso-8859-1")


df = df.iloc[:, 2:]
ultimo_cuartil = df.quantile(0.75)
percentil_80 = df.quantile(0.8)
print("---------- CON PANDAS ----------")
print("Ultimo cuartil por columna:")
print(ultimo_cuartil)
print("\nPercentil 80 por columna:")
print(percentil_80)

print("---------- CON NUMPY ----------")
data_array = df.values
ultimo_cuartil = np.nanpercentile(data_array, 75, axis=0)
percentil_80 = np.nanpercentile(data_array, 80, axis=0)
max_longitud_nombre = max(len(nombre) for nombre in df.columns)
print("Ultimo cuartil por columna:")
for columna, cuartil in zip(df.columns, ultimo_cuartil):
    print(f"{columna.ljust(max_longitud_nombre)}: {cuartil}")
print("\nPercentil 80 por columna:")
for columna, perc_80 in zip(df.columns, percentil_80):
    print(f"{columna.ljust(max_longitud_nombre)}: {perc_80}")

# C
media = df.mean()
mediana = df.median()
moda = df.mode().iloc[0]
media_geometrica = np.exp(np.mean(np.log(df), axis=0))
print("Media:")
print(media)
print("\nMediana:")
print(mediana)
print("\nModa:")
print(moda)
print("\nMedia geometrica:")
print(media_geometrica)

# D
df.hist(figsize=(12, 10))
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
