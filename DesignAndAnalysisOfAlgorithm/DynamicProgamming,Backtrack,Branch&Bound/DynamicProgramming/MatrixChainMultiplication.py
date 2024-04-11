def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    INF = float('inf')  # Infinity
    m = [[0] * (n+1) for _ in range(n+1)]
    s = [[0] * (n+1) for _ in range(n+1)]

    for chain_length in range(2, n+1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')

# Example usage
matrix_sizes = [4,10,3,12,2]
m, s = matrix_chain_order(matrix_sizes)
print("Minimum number of scalar multiplications:", m[1][len(matrix_sizes) - 1])
print("Optimal Parenthesization:", end=' ')
print_optimal_parens(s, 1, len(matrix_sizes) - 1)
