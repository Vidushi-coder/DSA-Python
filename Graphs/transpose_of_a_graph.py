# transpose of adjancy list representation of a graph

def addEdge(adj,src,des):
    adj[src].append(des)

def displayGraph(adj,vertices):
    for i in range(vertices):
        print(f"{i}:", end=" ")
        for j in adj[i]:
            print(j, end=" ")
        print()

def transposeGraph(adj,transpose,vertices):
    for i in range(vertices):
        for j in range(len(adj[i])):
            addEdge(transpose,adj[i][j],i)

if __name__ == "__main__":

    v = 5
    adj = [[] for _ in range(v)]

    addEdge(adj,0,1)
    addEdge(adj,0,4)    
    addEdge(adj,1,2)
    addEdge(adj,1,3)
    addEdge(adj,2,4)
    addEdge(adj,3,4)

    print("Original Graph:")
    displayGraph(adj, v)

    transpose = [[] for _ in range(v)]
    transposeGraph(adj, transpose, v)

    print("\nTranspose Graph:")
    displayGraph(transpose, v)

print("\n\n")
    
# transpose of adjancy matrix representation of a graph

def createGraph(vertices, edges):
    mat = [[0 for _ in range(vertices)] for _ in range(vertices)]

    for i in edges:
        u = i[0]
        v = i[1]    

        mat[u][v] = 1
        mat[v][u] = 1

    return mat

def displayGraph(mat, vertices):
    for i in range(vertices):
        for j in range(vertices):
            print(mat[i][j], end=" ")
        print()

def transposeGraph(mat, transpose, vertices):
    for i in range(vertices):
        for j in range(vertices):
            transpose[j][i] = mat[i][j]

if __name__ == "__main__":

    v = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 4), (3, 4)]
    mat = createGraph(v, edges)

    print("Original Graph:")
    displayGraph(mat, v)

    transpose = [[0 for _ in range(v)] for _ in range(v)]
    transposeGraph(mat, transpose, v)

    print("\nTranspose Graph:")
    displayGraph(transpose, v)