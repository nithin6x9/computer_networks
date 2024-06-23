import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    previous_nodes = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def plot_graph(graph, start_vertex, shortest_paths):
    G = nx.Graph()

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
    shortest_paths, previous_nodes = dijkstra(graph, start_vertex)
    
    print(f"Shortest paths from {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Distance to {vertex}: {distance}")

    plot_graph(graph, start_vertex, shortest_paths)


'''import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (dista

    # Dictionary to hold the shortest path to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Dictionary to hold the previous node in the optimal path
    previous_nodes = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can be added multiple times to the priority queue, we only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def plot_graph(graph, start_vertex, shortest_paths):
    G = nx.Graph()

    # Add edges to the graph
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    # Draw the graph
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)

    # Highlight the shortest paths
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

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    shortest_paths, previous_nodes = dijkstra(graph, start_vertex)
    
    print(f"Shortest paths from {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Distance to {vertex}: {distance}")

    plot_graph(graph, start_vertex, shortest_paths)
'''