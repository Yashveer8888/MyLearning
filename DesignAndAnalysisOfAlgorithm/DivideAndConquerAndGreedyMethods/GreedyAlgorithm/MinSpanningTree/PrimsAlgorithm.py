import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    priority_queue = []
    minimum_spanning_tree = []
    parent = [None] * n  # Initialize parent array to keep track of parent vertices
    
    # Start from vertex 0 (can be any arbitrary starting vertex)
    start_vertex = 0
    heapq.heappush(priority_queue, (0, start_vertex, start_vertex))  # Push (weight, parent, vertex) tuple into priority queue
    
    while priority_queue:
        weight, p, u = heapq.heappop(priority_queue)  # Extract minimum weight edge and parent vertex
        if not visited[u]:
            visited[u] = True
            if u != start_vertex:
                minimum_spanning_tree.append((p, u, weight))  # Add edge to minimum spanning tree
            
            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(priority_queue, (w, u, v))  # Push (weight, parent, vertex) tuple into priority queue
    
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

mst = prim(graph)
print("Minimum Spanning Tree (Prim's Algorithm):")
for p, u, weight in mst:
    print(f"Edge ({p}, {u}) with weight {weight}")
