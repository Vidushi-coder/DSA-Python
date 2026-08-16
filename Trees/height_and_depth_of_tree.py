class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)

    # Height of the tree
    def height(node):
        if node is None or not node.children:
            return 0
        else:
            heights = []
            for child in node.children:
                heights.append(Tree.height(child))
            return 1 + max(heights)
        
    # Depth of the tree
    def depth(node, target_value, current_depth=0): 
        if node is None:
            return -1
        if node.value == target_value:
            return current_depth
        for child in node.children:
            depth_of_child = Tree.depth(child, target_value, current_depth + 1)
            if depth_of_child != -1:
                return depth_of_child
        return -1

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

print("Height of the tree:", Tree.height(A))
print("Height of node B:", Tree.height(B))
print("Height of node D:", Tree.height(D))

print("Depth of node A:", Tree.depth(A, "A"))
print("Depth of node B:", Tree.depth(A, "B"))   
print("Depth of node D:", Tree.depth(A, "D"))