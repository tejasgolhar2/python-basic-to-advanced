def min_swaps_to_beautiful(array):
    n = len(array)

    # Count the number of elements out of order in ascending order
    asc_count = sum(1 for i in range(n - 1) if array[i] > array[i + 1])

    # Count the number of elements out of order in descending order
    desc_count = sum(1 for i in range(n - 1) if array[i] < array[i + 1])

    # If the array is already beautiful, no swaps are needed
    if asc_count == 0 or desc_count == 0:
        return 0

    # The minimum number of swaps is half of the count of elements out of order
    return min(asc_count, desc_count) // 2

# Example usage:
arr = [1, 5, 4, 3, 2]
result = min_swaps_to_beautiful(arr)
print(f"Minimum swap operations needed: {result}")
