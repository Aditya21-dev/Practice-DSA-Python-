def longest_subarray_sum_k(arr, K):
    prefix_map = {}   # stores {prefix_sum: first_index}
    current_sum = 0
    max_length = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        # Case 1: if sum itself equals K
        if current_sum == K:
            max_length = i + 1

        # Case 2: check if (current_sum - K) seen before
        if (current_sum - K) in prefix_map:
            length = i - prefix_map[current_sum - K]
            max_length = max(max_length, length)

        # Store only first occurrence
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length


# Example
arr = [10, 5, 2, 7, 1, 9]
K = 15
print(longest_subarray_sum_k(arr, K))