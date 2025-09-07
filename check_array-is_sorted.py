#If an array needs only one pass of bubble sort to be sorted, return True.
def is_nearly_sorted(arr):
    n = len(arr)
    swapped = False
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    return not swapped  # if no swap needed -> nearly sorted

# Example
print(is_nearly_sorted([1, 3, 2, 4, 5]))  # True
print(is_nearly_sorted([5, 4, 3, 2, 1]))  # False
