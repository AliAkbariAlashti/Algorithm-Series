def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        curr = arr[i]
        rest = arr[:i] + arr[i + 1:]
        for p in permutations(rest):
            result.append([curr] + p)
    return result

def combinations(arr, k):
    if k == 0:
        return [[]]
    if not arr:
        return []
    result = []
    for i in range(len(arr)):
        curr = arr[i]
        for c in combinations(arr[i + 1:], k - 1):
            result.append([curr] + c)
    return result

# Example usage
letters = ['A', 'B', 'C']
print("Permutations:", permutations(letters))
print("Combinations (k=2):", combinations(letters, 2))