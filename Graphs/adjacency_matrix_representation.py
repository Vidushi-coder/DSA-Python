#undirected graph representation using adjacency matrix

def createGraph(vertices, edges):
    mat = [[0 for _ in range(vertices)] for _ in range(vertices)]

    for i in edges:
        mat[i[0]][i[1]] = 1
        mat[i[1]][i[0]] = 1

    return mat

vertice = 5
graph = createGraph(vertice, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
for i in range(vertice):
    for j in range(vertice):
        print(graph[i][j], end=" ")
    print()


#directed graph representation using adjacency matrix

def createGraph(vertices, edges):
    mat = [[0 for _ in range(vertices)] for _ in range(vertices)]

    for i in edges:
        mat[i[0]][i[1]] = 1

    return mat

print()
print("Directed Graph:")
vertice = 5
graph = createGraph(vertice, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
for i in range(vertice):
    for j in range(vertice):
        print(graph[i][j], end=" ")
    print()