def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # no swaps -> already sorted
            break
    return arr

# Example
arr = [5, 1, 4, 2, 8]
print("Optimized Sorted:", bubble_sort_optimized(arr))
