def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:  # only change comparison
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
arr = [10, 7, 8, 9, 1, 5]
print("Descending Sorted:", bubble_sort_desc(arr))
