class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self):
        print(self.value)
        for child in self.children:
            child.print_tree()


def diameter(root):
    current_diameter = 0

    def max_depth(node):
        nonlocal current_diameter

        if node is None:
            return 0

        # Store heights of all children
        child_depths = []

        for child in node.children:
            child_depths.append(max_depth(child))

        # Find the two largest child heights
        child_depths.sort(reverse=True)

        if len(child_depths) >= 2:
            diameter = child_depths[0] + child_depths[1] + 2
        elif len(child_depths) == 1:
            diameter = child_depths[0] + 1
        else:
            diameter = 0

        # Update maximum diameter
        current_diameter = max(current_diameter, diameter)

        # Return height of current node
        if child_depths:
            return 1 + child_depths[0]
        else:
            return 0

    max_depth(root)

    return current_diameter


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

print("Diameter of the tree:", diameter(A))