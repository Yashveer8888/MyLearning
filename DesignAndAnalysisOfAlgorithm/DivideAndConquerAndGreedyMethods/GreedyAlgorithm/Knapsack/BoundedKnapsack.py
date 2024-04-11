def bounded_knapsack(items, capacity):
    n = len(items)
    Q = max(item['quantity'] for item in items)
    dp = [[[0 for _ in range(Q + 1)] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            for k in range(min(items[i - 1]['quantity'], j // items[i - 1]['weight']) + 1):
                if k * items[i - 1]['weight'] <= j:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i - 1][j - k * items[i - 1]['weight']][k] + k * items[i - 1]['value']
                    )
                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    return dp[n][capacity][Q]

# Example usage
items = [
    {'weight': 10, 'value': 60, 'quantity': 3},  # Item 1 with weight 10, value 60, and 3 copies available
    {'weight': 20, 'value': 100, 'quantity': 2},  # Item 2 with weight 20, value 100, and 2 copies available
    {'weight': 30, 'value': 120, 'quantity': 1}  # Item 3 with weight 30, value 120, and 1 copy available
]
knapsack_capacity = 50

max_value = bounded_knapsack(items, knapsack_capacity)
print("Maximum value (Bounded Knapsack Problem):", max_value)
