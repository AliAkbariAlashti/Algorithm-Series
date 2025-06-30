from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

# Example usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print("Path exists:", bfs(graph, 'A', 'D'))