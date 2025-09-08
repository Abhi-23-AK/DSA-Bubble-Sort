def bubble_sort_with_passes(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        print(f"Pass {i+1}: {arr}")
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example
arr = [5, 3, 8, 4, 2]
print("Final Sorted:", bubble_sort_with_passes(arr))
