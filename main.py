
from collections import defaultdict, deque
def longest_path(graph:list) -> int:
    n = len(graph)
    
    in_degree = [0] * n
    for u in range(n):
        for v, w in graph[u]:
            in_degree[v] += 1
    
    topo_order = []
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, w in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    dp = [float('-inf')] * n
    dp[topo_order[0]] = 0 
    
    for u in topo_order:
        if dp[u] != float('-inf'):
            for v, w in graph[u]:
                dp[v] = max(dp[v], dp[u] + w)
    
    longest_path_length = max(dp)
    
    return longest_path_length

graph =  [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
result = longest_path(graph)
print( result)
