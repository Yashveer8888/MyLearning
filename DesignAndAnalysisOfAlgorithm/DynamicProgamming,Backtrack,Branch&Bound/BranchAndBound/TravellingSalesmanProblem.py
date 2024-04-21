def permutations(arr, start, end):
    if start == end:
        yield arr[:]
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]
            yield from permutations(arr, start + 1, end)
            arr[start], arr[i] = arr[i], arr[start]

def travelling_salesman(graph):
    num_cities = len(graph)
    min_path = float('inf')
    optimal_path = []

    for perm in permutations(list(range(num_cities)), 0, num_cities - 1):
        current_pathweight = 0
        for i in range(num_cities - 1):
            current_pathweight += graph[perm[i]][perm[i + 1]]
        current_pathweight += graph[perm[-1]][perm[0]]

        if current_pathweight < min_path:
            min_path = current_pathweight
            optimal_path = perm[:]

    return min_path, optimal_path

# Example usage
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
min_weight, optimal_route = travelling_salesman(graph)
print("Minimum Path Weight:", min_weight)
print("Optimal Route:", optimal_route)
