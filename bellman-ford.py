import matplotlib.pyplot as plt
import networkx as nx

def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    previous_nodes[neighbor] = vertex

    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances, previous_nodes

def plot_graph(graph, start_vertex, shortest_paths):
    G = nx.DiGraph()

    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)

    for target, path_length in shortest_paths.items():
        if target == start_vertex:
            continue
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path = path[::-1]
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], width=3, edge_color='r')

    plt.title(f"Shortest Paths from {start_vertex}")
    plt.show()

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    try:
        shortest_paths, previous_nodes = bellman_ford(graph, start_vertex)
        
        print(f"Shortest paths from {start_vertex}:")
        for vertex, distance in shortest_paths.items():
            print(f"Distance to {vertex}: {distance}")

        plot_graph(graph, start_vertex, shortest_paths)
    except ValueError as e:
        print(e)
