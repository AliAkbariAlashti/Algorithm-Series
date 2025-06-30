def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
catalog = [10, 20, 30, 40, 42, 50, 60]
target = 42
result = binary_search(catalog, target)
print("Page found at index:", result)