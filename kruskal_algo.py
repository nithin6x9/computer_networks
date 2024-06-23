import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    edges = [(weight, u, v) for u in graph for v, weight in graph[u].items()]
    edges.sort()

    mst = []
    uf = UnionFind(len(graph))
    vertices = list(graph.keys())
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}

    for weight, u, v in edges:
        if uf.find(vertex_index[u]) != uf.find(vertex_index[v]):
            uf.union(vertex_index[u], vertex_index[v])
            mst.append((u, v, weight))

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

    mst_edges = [(u, v) for u, v, weight in mst]
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

    mst = kruskal(graph)

    print("Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")

    plot_graph(graph, mst)
