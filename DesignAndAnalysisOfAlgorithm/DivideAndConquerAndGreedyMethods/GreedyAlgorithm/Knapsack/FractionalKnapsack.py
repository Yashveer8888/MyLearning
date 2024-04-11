def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratios
    for item in items:
        item['ratio'] = item['value'] / item['weight']
    #print(items)

    # Sort items by value-to-weight ratios in descending order
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for item in items:
        if item['weight'] <= remaining_capacity:
            total_value += item['value']
            remaining_capacity -= item['weight']
        else:
            fraction = remaining_capacity / item['weight']
            total_value += fraction * item['value']
            break

    return total_value

# Example usage
items = [
    {'weight': 10, 'value': 60},
    {'weight': 20, 'value': 100},
    {'weight': 30, 'value': 120}
]
knapsack_capacity = 50

max_value = fractional_knapsack(items, knapsack_capacity)
print("Maximum value:", max_value)
