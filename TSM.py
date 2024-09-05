from graphviz import Digraph
import itertools

# Función para generar un ID incremental
node_id = 1
def inc():
    global node_id
    node_id += 1
    return str(node_id)

# Función para calcular la distancia total de un camino
def calculate_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # Regreso al nodo inicial
    return distance

# Función para resolver el TSP con fuerza bruta y generar el árbol de búsqueda con Graphviz
def tsp_brute_force_with_graph(graph, start):
    dot = Digraph(comment='TSP Tree', format='png')
    global node_id
    node_id = 1  # Reiniciar el ID del nodo

    nodes = list(graph.keys())
    nodes.remove(start)  # Remover el nodo inicial de las permutaciones
    min_path = None
    min_distance = float('inf')

    # Generar el árbol de búsqueda
    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)
        current_distance = calculate_distance(path, graph)

        # Crear nodos y aristas en el grafo
        path_label = ' -> '.join(path) + f" (Cost: {current_distance})"
        path_id = inc()
        dot.node(path_id, label=path_label)

        # Conectar con nodo anterior si existe
        if min_path:
            dot.edge(prev_path_id, path_id)

        # Mantener el camino con la distancia mínima
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = path
            min_path_id = path_id

        prev_path_id = path_id

    # Marcar el camino más corto en rojo
    dot.node(min_path_id, label=' -> '.join(min_path) + f" (Cost: {min_distance})", color='red', style='filled', fillcolor='lightcoral')

    dot.render('output/tsp_tree')  # Guardar la imagen del grafo en un archivo

    print(f"Camino más corto: {' -> '.join(min_path)}")
    print(f"Distancia más corta: {min_distance}")
    return dot

# Grafo de ejemplo basado en la imagen proporcionada
graph = {
    'A': {'B': 4, 'C': 1, 'D': float('inf'), 'E': 3},
    'B': {'A': 4, 'C': float('inf'), 'D': 5, 'E': 2},
    'C': {'A': 1, 'B': float('inf'), 'D': 3, 'E': 2},
    'D': {'A': float('inf'), 'B': 5, 'C': 3, 'E': 1},
    'E': {'A': 3, 'B': 2, 'C': 2, 'D': 1}
}

# Ejemplo de uso
dot = tsp_brute_force_with_graph(graph, 'A')
dot.view()  # Esto abrirá la imagen del grafo generado
