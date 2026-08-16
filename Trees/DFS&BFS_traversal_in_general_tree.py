class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)

    # DFS Traversal
    def dfs(node):
        if node is None:
            return
        print(node.value)
        for child in node.children:
            Tree.dfs(child)

    # BFS Traversal
    def bfs(node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while queue:
            current_node = queue.pop(0)
            print(current_node.value)
            for child in current_node.children:
                queue.append(child)

A = Tree("A")
B = Tree("B")
C = Tree("C")
D = Tree("D")
E = Tree("E")
F = Tree("F")
G = Tree("G")

A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(G)

print("DFS Traversal of the tree:")
Tree.dfs(A)

print("\nBFS Traversal of the tree:")
Tree.bfs(A)