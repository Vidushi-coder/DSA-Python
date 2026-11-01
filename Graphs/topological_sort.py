# topological sort for acyclic directed graphs (DAGs)

class Graph:
    def __init__(self,edges,n):

        self.adj_list = [[] for _ in range(n)]
        self.indegrees = [0] * n

        for src,dest in edges:
            self.adj_list[src].append(dest)
            self.indegrees[dest] += 1

def topological_sort(graph,path,visited,n):
    for v in range(n):

        if graph.indegrees[v] == 0 and not visited[v]:

            for neighbour in graph.adj_list[v]:
                graph.indegrees[neighbour] -= 1

            path.append(v)
            visited[v] = True

            topological_sort(graph,path,visited,n)

            for neighbour in graph.adj_list[v]:
                graph.indegrees[neighbour] += 1

            path.pop()
            visited[v] = False

    if len(path) == n:
        print(path)

def print_all_topological_sorts(graph):
    n = len(graph.adj_list)
    path = []
    visited = [False] * n
    topological_sort(graph,path,visited,n)

if __name__ == "__main__":
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    n = 6
    graph = Graph(edges,n)
    print_all_topological_sorts(graph)