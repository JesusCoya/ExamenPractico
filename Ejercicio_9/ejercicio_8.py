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
    [0,  3, 2, 5],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [5, 2, 5, 2],
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
