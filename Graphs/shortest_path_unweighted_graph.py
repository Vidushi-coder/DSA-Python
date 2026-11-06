# shortest path in weighted graph using bfs

from collections import deque

def bfs(graph,src,parent,dist):

    queue = deque()
    queue.append(src)

    dist[src] = 0

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if dist[neighbour] == 1e9:
                parent[neighbour] = node
                dist[neighbour] = dist[node] + 1
                queue.append(neighbour)

def printShortestDistance(graph,src,dest,vertex):
    parent = [-1]*vertex
    dist = [1e9]*vertex

    bfs(graph,src,parent,dist)

    if dist[dest] == 1e9:
        print("No path found")
        return

    path = []
    current = dest
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print("Shortest path:", path)

if __name__ == "__main__":
    vertex = 8
    edge = 10
    source = 2
    destination = 6 
    edges = [[0, 1], [1, 2], [0, 3], [3, 4], [4, 7], [3, 7], [6, 7], [4, 5], [4, 6], [5, 6]]

    graph = [[] for _ in range(vertex)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    printShortestDistance(graph, source, destination, vertex)