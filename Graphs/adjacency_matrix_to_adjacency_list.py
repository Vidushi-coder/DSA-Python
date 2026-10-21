def matToAdj(matrix):
    adj=[]
    v = len(matrix)
    
    for i in range(v):
        row = []
        for j in range(v):
            if matrix[i][j] == 1:
                row.append(j)

        adj.append(row)
    return adj

if __name__ == "__main__":
    matrix = [[0, 1, 1, 0, 0],
              [1, 0, 0, 1, 1],
              [1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0]]

    adj = matToAdj(matrix)
    print("Adjacency List of the graph is:")
    for i in range(len(adj)):
        print(i, "->", adj[i])