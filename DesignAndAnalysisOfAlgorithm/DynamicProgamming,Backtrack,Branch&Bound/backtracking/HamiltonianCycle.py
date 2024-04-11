def is_valid(v, graph, path, pos):
    # Check if vertex v can be added to the path
    if graph[path[pos-1]][v] == 0:
        return False
    
    # Check if vertex v is already in the path
    if v in path:
        return False
    
    return True

def hamiltonian_cycle_util(graph, path, pos, N):
    # Base case: All vertices are added to the path
    if pos == N:
        # Check if the last vertex connects back to the starting vertex
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    
    for v in range(N):
        if is_valid(v, graph, path, pos):
            # Add vertex v to the path
            path[pos] = v
            
            # Recur for the next position
            if hamiltonian_cycle_util(graph, path, pos+1, N):
                return True
            
            # Backtrack: Remove v from the path if no solution is found
            path[pos] = -1
    
    return False

def hamiltonian_cycle(graph):
    N = len(graph)
    path = [-1] * N  # Initialize path with -1
    
    # Start with the first vertex as the starting point
    path[0] = 0
    
    # Call the utility function to find Hamiltonian cycle
    if not hamiltonian_cycle_util(graph, path, 1, N):
        print("Solution does not exist")
        return False
    
    # Print the Hamiltonian cycle
    print("Hamiltonian cycle exists:")
    print(' '.join(map(str, path)))
    
    return True

# Example usage
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]
hamiltonian_cycle(graph)
