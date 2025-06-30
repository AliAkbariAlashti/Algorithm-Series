def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
books = [23, 15, 42, 19, 7]
target = 42
result = linear_search(books, target)
print("Book found at index:", result)