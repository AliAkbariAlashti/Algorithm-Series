def dfs(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    if node == target:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

# Example usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print("Path exists:", dfs(graph, 'A', 'D'))