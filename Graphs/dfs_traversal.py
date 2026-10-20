# dfs traversal of a connected graph

def dfsRec(adj,visited,src,res):
    visited[src]=True
    res.append(src)

    for i in adj[src]:
        if not visited[i]:
            dfsRec(adj,visited,i,res)

def dfs(adj):
    v = len(adj)
    visited = [False] * v
    res = []
    dfsRec(adj, visited, 0, res)
    return res

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    v = 5
    adj = [[] for i in range(v)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)

    print("DFS traversal of the graph is:", dfs(adj))

# dfs traversal of a disconnected graph

def dfsRec(adj,visited,src,res):
    visited[src]=True
    res.append(src)

    for i in adj[src]:
        if not visited[i]:
            dfsRec(adj,visited,i,res)

def dfs(adj):
    v = len(adj)
    visited = [False] * v
    res = []

    for i in range(v):
        if not visited[i]:
            dfsRec(adj, visited, i, res)

    return res

if __name__ == "__main__":
    v = 5
    adj = [[] for i in range(v)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)

    print("DFS traversal of the graph is:", dfs(adj))