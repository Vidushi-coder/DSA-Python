# Right side view
from collections import deque

# DFS Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def rightSideView(root,level,maxLevel,result):
    if root is None:
        return result

    if level>maxLevel[0]:
        result.append(root.data)
        maxLevel[0] = level

    rightSideView(root.right,level+1,maxLevel,result)
    rightSideView(root.left,level+1,maxLevel,result)

def rightView(root):
    result = []
    maxLevel = [-1]
    
    rightSideView(root, 0, maxLevel, result)
    
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    result = rightView(root)
    for val in result:
        print(val, end=" ")

# DFS Traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def rightSideView(root):
    result = []

    if root is None:
        return result

    q = deque([root])

    while q:
        level = len(q)

        for i in range(level):
            curr = q.popleft()

            if i == level - 1:
                result.append(curr.data)

            if curr.left is not None:
                q.append(curr.left) 

            if curr.right is not None:
                q.append(curr.right)    

    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    result = rightSideView(root)
    for val in result:
        print(val, end=" ")

# Left Side View

# DFS Traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftSideView(root,level,maxLevel,result):

    if root is None:
        return result

    if level > maxLevel[0]:
        result.append(root.data)
        maxLevel[0] = level    

    leftSideView(root.left,level+1,maxLevel,result)
    leftSideView(root.right,level+1,maxLevel,result)

def leftView(root):
    result = []
    maxLevel = [-1]

    leftSideView(root,0,maxLevel,result)

    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.right = Node(5)

    result = leftView(root)
    for val in result:
        print(val, end=" ")

# BFS Traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftSideView(root):
    result = []

    if root is None:
        return result

    q = deque([root])

    while q:
        level = len(q)

        for i in range(level):
            curr = q.popleft()

            if i == 0:
                result.append(curr.data)

            if curr.left is not None:
                q.append(curr.left) 

            if curr.right is not None:
                q.append(curr.right)    

    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.right = Node(5)

    result = leftSideView(root)
    for val in result:
        print(val, end=" ")                     