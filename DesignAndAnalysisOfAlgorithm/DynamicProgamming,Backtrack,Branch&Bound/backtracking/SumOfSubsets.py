def backtrack_subset_sum(nums, target, current_sum, start, subset, result):
    if current_sum == target:
        result.append(subset[:])  # Add a copy of the subset to the result
        return
    
    for i in range(start, len(nums)):
        if current_sum + nums[i] <= target:
            # Add the current element to the subset and update the current sum
            subset.append(nums[i])
            current_sum += nums[i]
            
            # Recur with the updated current sum and start index
            backtrack_subset_sum(nums, target, current_sum, i + 1, subset, result)
            
            # Backtrack: Remove the current element from the subset and restore the previous current sum
            current_sum -= subset.pop()

def find_subsets_with_sum(nums, target):
    result = []
    backtrack_subset_sum(nums, target, 0, 0, [], result)
    return result

# Example usage
nums = [2, 3, 5, 8]
target = 8
subsets_with_sum = find_subsets_with_sum(nums, target)
print("Subsets with sum", target, ":", subsets_with_sum)
