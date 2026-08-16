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

    def levelOrderTraversal(self):
        if self is None:
            return []
        
        queue = []
        result = []

        queue.append(self)
        current_level = 0

        while queue:
            result.append([])
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.pop(0)
                result[current_level].append(node.value)

                if node.left:
                    queue.append(node.left) 

                if node.right:
                    queue.append(node.right)

            current_level += 1

        return result

A = BinaryTreeNode("A")
A.insert_left("B")
A.insert_right("C")
B = A.left
C = A.right
B.insert_left("D")
B.insert_right("E")
C.insert_left("F")
C.insert_right("G")

print(A.levelOrderTraversal())