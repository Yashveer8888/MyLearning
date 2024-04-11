def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Initialize the table with zeros
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    for i in table:
        print(i)
    print()
        

    # Backtrack to find the LCS
    lcs_length = table[m][n]
    lcs = [""] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

# Example usage
X = "ABCBDA"
Y = "BDCAB"
result = longest_common_subsequence(X, Y)
print("Longest Common Subsequence (LCS):", result)
