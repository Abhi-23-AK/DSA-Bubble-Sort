#Standard bubble pushes largest to right; here we push smallest to right.
def reverse_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1, i, -1):  # loop backward
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Example
arr = [5, 1, 4, 2, 8]
print("Reverse Bubble Sorted:", reverse_bubble_sort(arr))
