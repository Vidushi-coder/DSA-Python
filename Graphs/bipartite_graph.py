#checking whether a given graph is bipartite or note

from collections import deque

def is_bipartite(graph):
    v = len(graph)
    colour = [-1]*v

    for i in range(v):
        if colour[i] == -1:
            queue = deque([i])
            colour[i] = 0

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    if colour[neighbour] == -1:
                        colour[neighbour] = 1 - colour[node]
                        queue.append(neighbour)

                    elif (colour[neighbour] == colour[node]):
                        return False

    return True

if __name__ == "__main__":
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(is_bipartite(graph))  

    graph = [[1, 2], [0, 2], [0, 1]]
    print(is_bipartite(graph))  