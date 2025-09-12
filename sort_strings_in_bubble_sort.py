#Bubble sort can also sort strings alphabetically.
def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:  # lexicographic compare
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
words = ["banana", "apple", "cherry", "date"]
print("Sorted Strings:", bubble_sort_strings(words))
