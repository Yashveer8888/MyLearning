class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative-weight cycle")
                return

        # Print the shortest distances
        self.print_distances(dist)

    def print_distances(self, dist):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    src_vertex = 0
    g.bellman_ford(src_vertex)
