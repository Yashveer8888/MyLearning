def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0  # Distance from a vertex to itself is 0

    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]
    for row in dist:
        print(row)
    print()

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and \
                        dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print(f"intermidiate vertices{k+1}")
        for row in dist:
            print(row)
        print()

    return dist

# Example usage:
graph = [
    [0, 3, 0, 7],
    [8, 0, 2, 0],
    [5, 0, 0, 1],
    [2, 0, 0, 0]
]

shortest_paths = floyd_warshall(graph)
print("final Answer")
for row in shortest_paths:
    print(row)
