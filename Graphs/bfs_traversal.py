from queue import deque

# BFS from given source in undirected graph
def bfs(adj):
    v = len(adj)
    visited = [False]*v
    result = []

    src = 0
    q = deque()
    visited[src] = True
    q.append(src) 

    while q:
        node = q.popleft()
        result.append(node)

        for x in adj[node]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return result

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

    print("BFS traversal of the graph is:", bfs(adj))

# BFS of disconnected undirected graph
def bfs_connected(adj,src,visited,result):
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        node = q.popleft()
        result.append(node)

        for i in adj[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def bfs(adj):
    v = len(adj)
    visited = [False]*v
    result = []

    for i in range(v):
        if not visited[i]:
            bfs_connected(adj,i,visited,result)

    return result

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    v = 7
    adj = [[] for i in range(v)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 5, 6)

    print("BFS traversal of the disconnected graph is:", bfs(adj))