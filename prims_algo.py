import heapq
import matplotlib.pyplot as plt
import networkx as nx

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))

    return mst

def plot_graph(graph, mst):
    G = nx.Graph()

    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)

    mst_edges = [(frm, to) for frm, to, weight in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color='r')

    plt.title("Minimum Spanning Tree")
    plt.show()

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    mst = prim(graph, start_vertex)

    print("Minimum Spanning Tree:")
    for frm, to, weight in mst:
        print(f"{frm} - {to}: {weight}")

    plot_graph(graph, mst)
