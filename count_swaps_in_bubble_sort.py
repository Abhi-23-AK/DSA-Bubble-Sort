#Return how many swaps Bubble Sort makes while sorting.
def count_swaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

# Example
arr = [6, 4, 1]
print("Swaps:", count_swaps(arr))  # Output: 3
