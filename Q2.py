def find_second_largest(arr):
    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None


# Example usage
arr = [10, 5, 20, 8, 15]
result = find_second_largest(arr)

if result is None:
    print("No second largest element")
else:
    print("Second Largest:", result)