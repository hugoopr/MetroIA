import matplotlib.pyplot as plt
import networkx as nx
import sys
from datetime import datetime, timedelta

# Definición del grafo
G = nx.Graph()

    # Añade nodos al grafo

    # Línea A
nodes_A = ['Vaulx-en-Velin La Soie', 'Laurent Bonnevay Astroballe', 'Cusset', 'Flachet', 'Gratte-Ciel', 'République Villeurbanne', 'Masséna', 'Foch', 'Cordeliers', 'Ampère Victor Hugo', 'Perrache']
G.add_nodes_from(nodes_A)

# Línea B
nodes_B = ['Oullins Gare', 'Stade de Gerland', 'Debourg', 'Place Jean Jaurès', 'Jean Macé', 'Place Guichard Bourse du Travail', 'Gare Part-Dieu Vivier Merle', 'Brotteaux']
G.add_nodes_from(nodes_B)

# Línea C
nodes_C = ['Cuire', 'Hénon', 'Croix-Rousse', 'Croix-Paquet']
G.add_nodes_from(nodes_C)

    # Línea D
nodes_D = ['Gare de Vaise', 'Valmy', 'Gorge de Loup', 'Vieux Lyon Cathédrale St.Jean', 'Guillotière', 'Garibaldi', 'Sans-Souci', 'Monplaisir-Lumière', 'Grange Blanche', 'Laënnec', 'Mermoz Pinel', 'Parilly', 'Gare de Vénissieux']
G.add_nodes_from(nodes_D)

    # Nodos trasbordo
nodes_join = ['Bellecour', 'Hôtel de Ville Louis Pradel', 'Charpennes Charles Hernu', 'Saxe Gambetta']
G.add_nodes_from(nodes_join)

    

    # Define los colores para los nodos
color_map = []
for node in G:
    if node in nodes_A:
        color_map.append('red')  # Colorea estos nodos de rojo
    elif node in nodes_B:
        color_map.append('blue')
    elif node in nodes_C:
        color_map.append('orange')  # Colorea estos nodos de naranja
    elif node in nodes_D:
        color_map.append('green')
    elif node in nodes_join:
        color_map.append('black')
    
pos = {
    'Gare de Vénissieux': (13, 0),
    'Parilly': (13, 3),
    'Mermoz Pinel': (13, 5.5),
    'Laënnec': (13, 8),
    'Grange Blanche': (12, 9),
    'Monplaisir-Lumière': (11, 10),
    'Sans-Souci': (10, 11),
    'Garibaldi': (9, 12),
    'Guillotière': (7, 13.25),
    'Gare de Vaise': (0, 19.5),
    'Valmy': (0, 18),
    'Gorge de Loup': (0, 16),
    'Vieux Lyon Cathédrale St.Jean': (5.5, 14),
    'Cuire': (6, 22),
    'Hénon': (5.5, 19),
    'Croix-Rousse': (6, 18),
    'Croix-Paquet': (6.5, 17),
    'Vaulx-en-Velin La Soie': (18, 14.5),
    'Laurent Bonnevay Astroballe': (16, 15),
    'Cusset': (15, 15.5),
    'Flachet': (14, 16),
    'Gratte-Ciel': (13, 16.5),
    'République Villeurbanne': (12, 17),
    'Masséna': (9, 17),
    'Foch': (7.5, 16.5),
    'Hôtel de Ville Louis Pradel': (6.5, 16),
    'Cordeliers': (6.5, 15),
    'Bellecour': (6, 13.5),
    'Ampère Victor Hugo': (5, 12.5),
    'Perrache': (4, 11.5),
    'Charpennes Charles Hernu': (10, 17),
    'Brotteaux': (9.5, 16),
    'Gare Part-Dieu Vivier Merle': (9, 15),
    'Place Guichard Bourse du Travail': (8, 14),
    'Saxe Gambetta': (8, 13),
    'Jean Macé': (7, 11),
    'Place Jean Jaurès': (6, 9),
    'Debourg': (5, 7),
    'Stade de Gerland': (4, 5),
    'Oullins Gare': (1, 2)
}


edges_linea_A = [
    ("Vaulx-en-Velin La Soie", "Laurent Bonnevay Astroballe", {'distancia': 1.1, 'tiempo': 2}),
    ("Laurent Bonnevay Astroballe", "Cusset", {'distancia': 0.7, 'tiempo': 1}),
    ("Cusset", "Flachet", {'distancia': 0.9, 'tiempo': 2}),
    ("Flachet", "Gratte-Ciel", {'distancia': 0.6, 'tiempo': 1}),
    ("Gratte-Ciel", "République Villeurbanne", {'distancia': 0.7, 'tiempo': 1}),
    ("République Villeurbanne", "Charpennes Charles Hernu", {'distancia': 0.8, 'tiempo': 2}),
    ("Charpennes Charles Hernu", "Masséna", {'distancia': 0.8, 'tiempo': 1}),
    ("Masséna", "Foch", {'distancia': 0.7, 'tiempo': 2}),
    ("Foch", "Hôtel de Ville Louis Pradel", {'distancia': 0.7, 'tiempo': 1}),
    ("Hôtel de Ville Louis Pradel", "Cordeliers", {'distancia': 0.4, 'tiempo': 1}),
    ("Cordeliers", "Bellecour", {'distancia': 0.6, 'tiempo': 2}),
    ("Bellecour", "Ampère Victor Hugo", {'distancia': 0.6, 'tiempo': 1}),
    ("Ampère Victor Hugo", "Perrache", {'distancia': 0.5, 'tiempo': 1})
]
    # Línea B
edges_linea_B = [
    ("Oullins Gare", "Stade de Gerland", {'distancia': 1.8, 'tiempo': 4}),
    ("Stade de Gerland", "Debourg", {'distancia': 0.6, 'tiempo': 1}),
    ("Debourg", "Place Jean Jaurès", {'distancia': 0.7, 'tiempo': 2}),
    ("Place Jean Jaurès", "Jean Macé", {'distancia': 1, 'tiempo': 1}),
    ("Jean Macé", "Saxe Gambetta", {'distancia': 1, 'tiempo': 2}),
    ("Saxe Gambetta", "Place Guichard Bourse du Travail", {'distancia': 0.6, 'tiempo': 1}),
    ("Place Guichard Bourse du Travail", "Gare Part-Dieu Vivier Merle", {'distancia': 0.9, 'tiempo': 2}),
    ("Gare Part-Dieu Vivier Merle", "Brotteaux", {'distancia': 0.6, 'tiempo': 1}),
    ("Brotteaux", "Charpennes Charles Hernu", {'distancia': 0.5, 'tiempo': 2})
]

    # Línea C
edges_linea_C = [
    ("Hôtel de Ville Louis Pradel", "Croix-Paquet", {'distancia': 0.4, 'tiempo': 2}),
    ("Croix-Paquet", "Croix-Rousse", {'distancia': 0.5, 'tiempo': 2}),
    ("Croix-Rousse", "Hénon", {'distancia': 0.7, 'tiempo': 2}),
    ("Hénon", "Cuire", {'distancia': 0.8, 'tiempo': 3})
]
    # Línea D
edges_linea_D = [
    ("Gare de Vaise", "Valmy", {'distancia': 0.6, 'tiempo': 2}),
    ("Valmy", "Gorge de Loup", {'distancia': 1, 'tiempo': 2}),
    ("Gorge de Loup", "Vieux Lyon Cathédrale St.Jean", {'distancia': 1.7, 'tiempo': 2}),
    ("Vieux Lyon Cathédrale St.Jean", "Bellecour", {'distancia': 0.7, 'tiempo': 1}),
    ("Bellecour", "Guillotière", {'distancia': 0.8, 'tiempo': 1}),
    ("Guillotière", "Saxe Gambetta", {'distancia': 0.4, 'tiempo': 1}),
    ("Saxe Gambetta", "Garibaldi", {'distancia': 0.6, 'tiempo': 1}),
    ("Garibaldi", "Sans-Souci", {'distancia': 1, 'tiempo': 1}),
    ("Sans-Souci", "Monplaisir-Lumière", {'distancia': 0.5, 'tiempo': 1}),
    ("Monplaisir-Lumière", "Grange Blanche", {'distancia': 0.7, 'tiempo': 1}),
    ("Grange Blanche", "Laënnec", {'distancia': 0.8, 'tiempo': 1}),
    ("Laënnec", "Mermoz Pinel", {'distancia': 0.9, 'tiempo': 1}),
    ("Mermoz Pinel", "Parilly", {'distancia': 1.2, 'tiempo': 2}),
    ("Parilly", "Gare de Vénissieux", {'distancia': 1.6, 'tiempo': 3})
]
lineas = [edges_linea_A,edges_linea_B,edges_linea_C,edges_linea_D]
# Añade aristas al grafo
G.add_edges_from(edges_linea_A)
G.add_edges_from(edges_linea_B)
G.add_edges_from(edges_linea_C)
G.add_edges_from(edges_linea_D)
horarioA = [4,37, 24,18]
horarioB = [4,49, 24,20]
horarioC = [5,00, 24,25]
horarioD = [5,00, 24,19]

horarios = [ horarioA,horarioB,horarioC,horarioD]
# Verificar si la hora está en alguno de los intervalos

def check_interval(interval,hora,minutos):
    if hora ==0:
        hora=24
    horaI, minutosI = interval[0],interval[1]
    horaS, minutosS = interval[2],interval[3]
    if horaI < hora < horaS:
            return True
    elif horaI == hora:
        if minutosI<= minutos:
            return True
    elif horaS == hora:
         if  minutos<minutosS:
             return True
    return False
#letra asociada a linea
def letrasociada(numero):
    if numero == 0:
        return "A"
    elif numero == 1:
        return "B"
    elif numero == 2:
        return "C"
    elif numero == 3:
        return "D"
    else :
        return None
# Algoritmo A*
def A_star(graph, start, goal,x):
    hora_in=x
    open_set = {start}
    came_from = {}
    tiempo_paradas = {}
    tiempo_paradas[start] = 0
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f = {node: float('inf') for node in graph.nodes}
    f[start] = nx.shortest_path_length(graph, start, goal, weight='tiempo')
    print("Este es el tiempo estimado del camino mas corto: ", f[start])

    while open_set  :
        current = None
        minimo = float('inf')
        for node in open_set:
            if f[node] < minimo:
                current = node
                minimo= f[node]       
        if current == goal:
            return reconstruct_path(came_from, current,hora_in,tiempo_paradas)
        
        open_set.remove(current)
        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph.edges[current, neighbor]['tiempo']
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                tiempo_paradas[neighbor] = graph.edges[current, neighbor]['tiempo']
                g_score[neighbor] = tentative_g_score
                f[neighbor] = g_score[neighbor] + nx.shortest_path_length(graph, neighbor, goal, weight='tiempo')
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return []

# Reconstrucción del camino
def reconstruct_path(came_from, current,hora,tiempo_paradas):
    path = [current]
    hora_in = datetime.strptime(hora, "%H:%M")
    
    while current in came_from:
        ind = encontrar_linea_del_nodo(current)
        intervalo = horarios[ind]
        hora_in += timedelta(minutes=tiempo_paradas[current])
        hora_str = hora_in.strftime("%H:%M")
        hora, minutos =  hora_str.split(':')
        if not check_interval(intervalo,int(hora),int(minutos)):
            letra = letrasociada(ind)
            letra = "No es posible realizar el trayecto en la hora seleccionada debido al cierre de la linea " + letra
            return letra
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path,hora_in
#funcion para saber a que intervalo pertenece un nodo
def encontrar_linea_del_nodo(nodo):
    for idx, linea in enumerate(lineas):
        for edge in linea:
            if nodo in edge[:2]:
                return idx
    return "No se encontró la línea para el nodo"
#funcion para obtener la linea a la que pertenece un nodo
def obtener_linea(nodo, lineas):
    for linea, nodos in lineas.items():
        if nodo in nodos:
            return linea
    return None
# Uso del algoritmo
if len(sys.argv) != 4:
    print("Numero equivocado de argumentos:",len(sys.argv))
    sys.exit()
else:
    inicio = sys.argv[1]
    fin = sys.argv[2]
    hora_inicio = sys.argv[3]
valor = A_star(G, inicio, fin,hora_inicio)
if len(valor)==2:
    path = valor[0]
    hora_fin = valor[1]
    print("Camino mas corto: ", path)
    print("Hora de llegada a",fin, "desde",inicio, ":",hora_fin.strftime("%H:%M"))
else:
    print(valor)
    sys.exit() 



# Visualización del grafo con el camino encontrado
plt.figure(figsize=(12, 8))  # Establece el tamaño de la figura
grados = dict(G.degree())
tamaño_base = 100
sizes = [tamaño_base * 2 if grados[node] > 2 else tamaño_base for node in G.nodes()]

# Dibuja el grafo
nx.draw(G, pos, node_color=color_map, node_size=sizes)
node_label_pos = {node: (pos[node][0], pos[node][1] - 0.25) for node in G.nodes()}  
nx.draw_networkx_labels(G, node_label_pos, font_size=8, font_color='black', font_weight='bold', verticalalignment='top')

# Dibuja todas las aristas en un color estándar
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', alpha=0.5)

# Resalta el camino más corto encontrado
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='purple', width=5)

nx.draw_networkx_edges(G, pos, edgelist=edges_linea_A, edge_color='red', width=1)

nx.draw_networkx_edges(G, pos, edgelist=edges_linea_B, edge_color='blue', width=1)

nx.draw_networkx_edges(G, pos, edgelist=edges_linea_C, edge_color='orange', width=1)

nx.draw_networkx_edges(G, pos, edgelist=edges_linea_D, edge_color='green')



# Muestra el grafo
plt.show();