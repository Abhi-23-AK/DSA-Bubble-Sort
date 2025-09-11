def bubble_sort_tuples(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j][1] > arr[j+1][1]:  # compare by 2nd element
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
arr = [(1, 3), (2, 1), (4, 2)]
print("Sorted by 2nd element:", bubble_sort_tuples(arr))
