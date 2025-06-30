def pagerank(graph, iters=100, d=0.85):
    n = len(graph)
    ranks = {node: 1/n for node in graph}
    for _ in range(iters):
        new_ranks = {}
        for node in graph:
            new_ranks[node] = (1 - d) / n
            for neighbor in graph:
                if node in graph[neighbor]:
                    new_ranks[node] += d * ranks[neighbor] / len(graph[neighbor])
        ranks = new_ranks
    return ranks

# Example usage
graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
print("PageRank:", pagerank(graph))