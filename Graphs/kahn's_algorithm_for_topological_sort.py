# kahn's algorithm for topological sort

from collections import deque

def topological_sort_kahn(adj):
    n = len(adj)
    indegree = [0]*n
    res = []
    queue = deque()

    for i in range(n):
        for j in adj[i]:
            indegree[j] += 1

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    while queue:    
        node = queue.popleft()
        res.append(node)

        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return res

def add_edge(adj, u, v):
    adj[u].append(v)

n = 6
adj = [[] for _ in range(n)]    

add_edge(adj, 5, 2)
add_edge(adj, 5, 0) 
add_edge(adj, 4, 0)
add_edge(adj, 4, 1)
add_edge(adj, 2, 3)
add_edge(adj, 3, 1)

result = topological_sort_kahn(adj)
if len(result) == n:
    print("Topological Sort:", result)
else:
    print("The graph has a cycle and topological sort is not possible.")