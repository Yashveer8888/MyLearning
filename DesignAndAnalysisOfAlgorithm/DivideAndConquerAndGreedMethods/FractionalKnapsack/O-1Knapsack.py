def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if items[i - 1]['weight'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]['weight']] + items[i - 1]['value'])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

# Example usage
items = [
    {'weight': 10, 'value': 60},
    {'weight': 20, 'value': 100},
    {'weight': 30, 'value': 120}
]
knapsack_capacity = 50

max_value = knapsack_01(items, knapsack_capacity)
print("Maximum value (0/1 Knapsack Problem):", max_value)
