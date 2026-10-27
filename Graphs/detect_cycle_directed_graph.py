# uisng dfs

def dfs(adj,u,visited,pathVisited):

    if pathVisited[u]:
        return True

    if visited[u]:
        return False

    visited[u] = True
    pathVisited[u] = True

    for neighbour in adj[u]:
        if dfs(adj,neighbour,visited,pathVisited):
            return True

    pathVisited[u] = False

    return False

def isCyclic(adj):
    v = len(adj)

    visited = [False]*v
    pathVisited = [False]*v

    for i in range(v):
        if not visited[i]:
            if dfs(adj,i,visited,pathVisited):
                return True

    return False

if __name__ == "__main__":
    adj = [[1],[2],[0,3],[4],[5],[3]]
    print(isCyclic(adj))


# using bfs

from collections import deque

def isCyclic(adj):
    v = len(adj)
    indegree = [0]*v

    queue = deque()
    visited = 0

    for i in range(v):
        for neighbour in adj[i]:
            indegree[neighbour] += 1

    for i in range(v):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        visited += 1

        for neighbour in adj[u]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return visited != v

if __name__ == "__main__":
    adj = [[1],[2],[0,3],[4],[5],[3]]
    print(isCyclic(adj))