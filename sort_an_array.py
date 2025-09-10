#Sort an array using the Bubble Sort algorithm.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # passes
        for j in range(n-1-i):  # compare adjacent
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Sorted:", bubble_sort(arr))
