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

    def level_order_traversal(self, level, result):
        if self is None:
            return
        
        if len(result) <= level:
            result.append([])

        result[level].append(self.value)
        if self.left:
            self.left.level_order_traversal(level + 1, result)
        if self.right:
            self.right.level_order_traversal(level + 1, result)

A = BinaryTreeNode("A")
A.insert_left("B")
A.insert_right("C")
B = A.left
C = A.right
B.insert_left("D")
B.insert_right("E")
C.insert_left("F")
C.insert_right("G")

result = []
A.level_order_traversal(0, result)
print(result)