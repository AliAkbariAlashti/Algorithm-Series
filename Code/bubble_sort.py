# Bubble Sort implementation for sorting a list in ascending order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Iterate through the list n times
        swapped = False  # Flag to optimize if no swaps occur
        for j in range(0, n - i - 1):  # Compare adjacent elements
            if arr[j] > arr[j + 1]:  # Swap if current element is larger
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps, list is sorted
            break
    return arr

# Example usage with a list of student heights (in cm)
heights = [160, 175, 155, 180, 165]
print("Original list:", heights)
sorted_heights = bubble_sort(heights)
print("Sorted list:", sorted_heights)