#Use Bubble Sort idea but stop after k passes.
def kth_largest(arr, k):
    n = len(arr)
    for i in range(k):  # only k passes
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[-k]

# Example
arr = [7, 10, 4, 3, 20, 15]
print("3rd Largest:", kth_largest(arr, 3))
