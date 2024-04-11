import heapq

def dijkstra(graph, source):
    n = len(graph)
    distances = [float('inf')] * n  # Initialize distances with infinity
    distances[source] = 0  # Distance from source to itself is 0
    visited = set()
    priority_queue = [(0, source)]  # Priority queue: (distance, vertex)

    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)  # Extract minimum distance vertex
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if v not in visited:
                new_distance = dist_u + weight
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    heapq.heappush(priority_queue, (new_distance, v))

    return distances

# Example usage
graph = [
    [(1, -1), (2, 4)],  # Edge format: (vertex, weight)
    [(4, 2), (3, 2), (2, 3)],
    [],
    [(2, 5), (1, 1)],
    [(3, -3)]
]
source_vertex = 0

shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from source vertex:")
for i, distance in enumerate(shortest_distances):
    print(f"Vertex {i}: {distance}")
