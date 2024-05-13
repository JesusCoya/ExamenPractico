from tabulate import tabulate


def cargar_datos(nombre_archivo):
    datos = []  # Lista para almacenar los datos
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = linea.strip().split(",")
            # Convertimos los elementos a los tipos de datos adecuados si es necesario
            fila = [
                (
                    int(elemento)
                    if elemento.isdigit()
                    else (
                        float(elemento)
                        if elemento.replace(".", "", 1).isdigit()
                        else elemento
                    )
                )
                for elemento in fila
            ]
            datos.append(fila)
    return datos


def imprimir_datos(datos):
    print(tabulate(datos, headers="firstrow", tablefmt="pretty"))


def obtener_columna(datos, indice_columna):
    return [fila[indice_columna] for fila in datos]


def calcular_cuartil(datos, indice_columna, cuartil):
    columna = obtener_columna(datos, indice_columna)
    # Filtrar solo los elementos que sean números
    columna_numerica = [
        elemento for elemento in columna if isinstance(elemento, (int, float))
    ]
    # Ordenar la columna numérica
    columna_numerica.sort()
    # Calcular el cuartil
    posicion_cuartil = int(len(columna_numerica) * cuartil)
    return columna_numerica[posicion_cuartil]


def calcular_percentil(datos, indice_columna, percentil):
    columna = obtener_columna(datos, indice_columna)

    # Filtrar solo los elementos que sean números
    columna_numerica = [
        elemento for elemento in columna if isinstance(elemento, (int, float))
    ]

    # Ordenar la columna numérica
    columna_numerica.sort()

    # Calcular el percentil
    posicion_percentil = int(len(columna_numerica) * percentil / 100)
    return columna_numerica[posicion_percentil]


# Ejemplo de uso
nombre_archivo = "Twitch_game_data.csv"
datos = cargar_datos(nombre_archivo)
# imprimir_datos(datos)
num_columnas = len(datos[0])
for i in range(num_columnas):
    if i > 3:
        ultimo_cuartil = calcular_cuartil(datos, i, 0.75)
        percentil_80 = calcular_percentil(datos, i, 80)
        print(f"Cuartil 3 (75%) de la columna {i + 1}: {ultimo_cuartil}")
        print(f"Percentil 80 de la columna {i + 1}: {percentil_80}")
        print()
