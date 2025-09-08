#Sort numbers based on absolute value using bubble sort.
def bubble_sort_abs(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if abs(arr[j]) > abs(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
arr = [-7, 1, -3, 4, -2]
print("Sorted by abs:", bubble_sort_abs(arr))
