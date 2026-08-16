class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)

    def print_tree(self):
        print(self.value)
        for child in self.children:
            child.print_tree()

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

A.print_tree()