def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def kruskal(graph, vertices):
    parent = {v: v for v in vertices}
    edges = sorted((w, u, v) for u in graph for v, w in graph[u])
    mst = []
    for w, u, v in edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            parent[pu] = pv
            mst.append((u, v, w))
    return mst

# Example usage
graph = {'A': [('B', 4), ('C', 2)], 'B': [('A', 4), ('C', 3), ('D', 5)], 
         'C': [('A', 2), ('B', 3), ('D', 8)], 'D': [('B', 5), ('C', 8)]}
vertices = ['A', 'B', 'C', 'D']
print("MST edges:", kruskal(graph, vertices))