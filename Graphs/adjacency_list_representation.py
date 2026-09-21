#undirected graph representation using adjacency list

def createGraph(vertices,edges):
    graph = [[] for _ in range(vertices)]

    for i in edges:
        u = i[0]
        v = i[1]

        graph[u].append(v)
        graph[v].append(u)

    return graph

vertice = 5
graph = createGraph(vertice, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
for i in range(vertice):
        print(f"{i}:", end=" ")
        for j in graph[i]:
            print(j, end=" ")
        print()

print()

#directed graph representation using adjacency list

def createGraph(vertices,edges):
    graph = [[] for _ in range(vertices)]

    for i in edges:
        u = i[0]
        v = i[1]

        graph[u].append(v)

    return graph

print("Directed Graph:")
vertice = 5
graph = createGraph(vertice, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
for i in range(vertice):
        print(f"{i}:", end=" ")
        for j in graph[i]:
            print(j, end=" ")
        print()