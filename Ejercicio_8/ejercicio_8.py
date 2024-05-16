import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def evalDistance(individual):
    suma = 0
    for i in range(len(individual)):
        if i == len(individual)-1:
            suma = suma+grafo[individual[i], individual[0]]
        else:
            suma = suma+grafo[individual[i], individual[i+1]]
    return suma


grafo = np.array([
    [0,  5, 0, 10, 3, 0, 2, 0],
    [5,	0,	7,	0, 5, 1, 0,	9],
    [0, 7, 0, 9, 0, 0, 0, 0],
    [10, 0, 9, 0, 6, 0,	14, 3],
    [3,	5, 0, 6, 0,	4, 6, 6],
    [0,	1, 0, 0, 4, 0, 12, 15],
    [2,	0, 0, 14, 6, 8, 0, 0],
    [0,	9, 0, 3, 6, 15,	0, 0]
])

# Genera todas las permutaciones de los nodos excepto el primero
nodos = list(range(1, len(grafo)))
permutaciones = itertools.permutations(nodos)

# Agrega el nodo inicial al principio de cada permutación
caminos = [[0] + list(p) for p in permutaciones]

# Mostrar por consola todos los caminos
print("Todos los caminos:")
for camino in caminos:
    print(camino, "Suma del camino: ", evalDistance(camino))


G = nx.DiGraph()
num_nodos = len(grafo)
G.add_nodes_from(range(num_nodos))

# Agrega bordes ponderados al grafo
for i in range(num_nodos):
    for j in range(num_nodos):
        if grafo[i][j] != 0:
            G.add_edge(i, j, weight=grafo[i][j])

# Dibuja el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue",
        font_size=12, font_weight="bold", arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo")
plt.show()
