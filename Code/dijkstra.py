from heapq import heappush, heappop

def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr = heappop(pq)
        if curr == target:
            return curr_dist
        if curr_dist > distances[curr]:
            continue
        for neighbor, weight in graph[curr]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    return distances[target]

# Example usage
graph = {'A': [('B', 4), ('C', 2)], 'B': [('D', 5)], 'C': [('D', 8)], 'D': []}
print("Shortest path cost:", dijkstra(graph, 'A', 'D'))