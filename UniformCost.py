from graphviz import Graph

# Variable global para el incremento del ID de los nodos
node_id = 1

# Función para generar un ID incremental
def inc():
    global node_id
    node_id += 1
    return str(node_id)

# Función para obtener los sucesores de un nodo dado
def sucesores(n):
    if n[0] == 'A':
        return [['B', n[1] + 3, inc()], ['C', n[1] + 2, inc()]]
    if n[0] == 'B':
        return [['A', n[1] + 3, inc()], ['C', n[1] + 2, inc()], ['D', n[1] + 2, inc()], ['E', n[1] + 1, inc()]]
    if n[0] == 'C':
        return [['A', n[1] + 2, inc()], ['B', n[1] + 2, inc()], ['E', n[1] + 5, inc()]]
    if n[0] == 'D':
        return [['B', n[1] + 2, inc()], ['E', n[1] + 2, inc()], ['F', n[1] + 4, inc()]]
    if n[0] == 'E':
        return [['B', n[1] + 1, inc()], ['C', n[1] + 5, inc()], ['D', n[1] + 2, inc()], ['F', n[1] + 1, inc()]]
    if n[0] == 'F':
        return [['D', n[1] + 4, inc()], ['E', n[1] + 1, inc()]]


# Función para generar el grafo usando Graphviz
def costo(start, end):
    dot = Graph(comment='Grafo', format='png')
    global node_id
    node_id = 1  # Reiniciar el ID del nodo
    list_nodes = [[start, 0, inc()]]
    dot.node(list_nodes[0][2], label=list_nodes[0][0])

    while len(list_nodes) > 0:
        current = list_nodes.pop(0)
        if current[0] == end:
            dot.render('output/graph')  # Guardar la imagen del grafo en un archivo
            return dot

        temp = sucesores(current)
        for val in temp:
            dot.node(val[2], label=val[0])
            dot.edge(current[2], val[2], label=str(val[1]))
        
        list_nodes = temp + list_nodes
        list_nodes = sorted(list_nodes, key=lambda x: x[1])

    dot.render('output/graph')  # Guardar la imagen del grafo en un archivo
    return dot

# Ejemplo de uso
dot = costo('A', 'F')
dot.view()  # Esto abrirá la imagen del grafo generado
