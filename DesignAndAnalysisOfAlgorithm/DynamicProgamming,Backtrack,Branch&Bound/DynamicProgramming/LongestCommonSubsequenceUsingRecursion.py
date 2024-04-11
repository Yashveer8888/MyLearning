def lcs_recursive(X, Y, m, n):
    # Base case: If either sequence is empty, return an empty string
    if m == 0 or n == 0:
        return ""
    # If last characters match, append the character to LCS and recurse
    elif X[m - 1] == Y[n - 1]:
        return lcs_recursive(X, Y, m - 1, n - 1) + X[m - 1]
    else:
        # If last characters don't match, consider both cases and choose the longer LCS
        lcs1 = lcs_recursive(X, Y, m - 1, n)
        lcs2 = lcs_recursive(X, Y, m, n - 1)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

# Example usage
X = "ABCBDAB"
Y = "BDCAB"
result = lcs_recursive(X, Y, len(X), len(Y))
print("Longest Common Subsequence (LCS):", result)
