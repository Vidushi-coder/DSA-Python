class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.right = self.right
            self.right = new_node

    def print_tree(self):
        print(self.value)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

A = BinaryTreeNode("A")
A.insert_left("B")
A.insert_right("C")
B = A.left
C = A.right
B.insert_left("D")
B.insert_right("E")
C.insert_left("F")
C.insert_right("G")

A.print_tree()