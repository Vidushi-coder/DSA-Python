# using dfs

def dfs(v,adj,visited,parent):
    visited[v] = True

    for neighbour in adj[v]:
        if not visited[neighbour]:
            if dfs(neighbour,adj,visited,v):
                return True

        elif neighbour != parent:
            return True

    return False

def detect_cycle(adj):
    v = len(adj)

    visited = [False]*v

    for i in range(v):
        if not visited[i]:
            if dfs(i,adj,visited,-1):
                return True

    return False

if __name__ == "__main__":
    adj = [[1,2],[0,2],[0,1,3],[2]]
    print(detect_cycle(adj))


# using bfs

from collections import deque
def bfs(v,adj,visited):
    q = deque()
    q.append((v,-1))
    visited[v] = True

    while q:
        node = q[0][0]
        parent = q[0][1]
        q.popleft()

        for neighbour in adj[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append((neighbour,node))

            elif parent != neighbour:
                return True

        return False

def detect_cycle(adj):
    v = len(adj)
    visited = [False]*v

    for i in range(v):
        if not visited[i]:
            if bfs(i,adj,visited):
                return True

    return False

if __name__ == "__main__":
    adj = [[1,2],[0,2],[0,1,3],[2]]
    print(detect_cycle(adj))