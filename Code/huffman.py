from heapq import heappush, heappop

def huffman_codes(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(heap[0][1:])

# Example usage
message = "AABBCC"
print("Huffman codes:", huffman_codes(message))