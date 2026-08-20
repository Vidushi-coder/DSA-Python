# BFS approach
from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def zigzagTraversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    leftToRight = True

    while queue:
        length = []
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            length.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not leftToRight:
            length.reverse()

        result.append(length)
        leftToRight = not leftToRight

    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    result = zigzagTraversal(root)
    for level in result:
        print(level)

# DFS approach

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    leftHeight = tree_height(root.left)
    rightHeight = tree_height(root.right)
    return max(leftHeight, rightHeight) + 1

def leftToRightTraversal(root,level,result):
    if root is None:
        return 

    if level == 1:
        result.append(root.data)
    else:
        leftToRightTraversal(root.left, level - 1, result)
        leftToRightTraversal(root.right, level - 1, result)

def rightToLeftTraversal(root,level,result):
    if root is None:
        return 

    if level == 1:
        result.append(root.data)
    else:
        rightToLeftTraversal(root.right, level - 1, result)
        rightToLeftTraversal(root.left, level - 1, result)

def zigzagTraversal(root):
    result = []
    leftToRight = True
    height = tree_height(root)

    for level in range(1, height + 1):
        if leftToRight:
            leftToRightTraversal(root, level, result)
        else:
            rightToLeftTraversal(root, level, result)

        leftToRight = not leftToRight

    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    result = zigzagTraversal(root)
    for val in result:
        print(val, end=" ")