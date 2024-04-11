class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    edges = []
    for u in range(len(graph)):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()

    n = len(graph)
    uf = UnionFind(n)
    minimum_spanning_tree = []

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

# Example usage
graph = [
    [(1, 7), (2, 8)],  # Edge format: (vertex, weight)
    [(0, 7), (2, 5), (3, 9), (4, 7)],
    [(0, 8), (1, 5), (4, 5)],
    [(1, 9), (4, 15), (5, 6)],
    [(1, 7), (2, 5), (3, 15), (5, 8), (6, 9)],
    [(3, 6), (4, 8), (6, 11)],
    [(4, 9), (5, 11)]
]

mst = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):")
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with weight {weight}")
