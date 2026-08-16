from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def printTree(root):
    if root is None:
        return ("[]")

    ans = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            ans.append("null")
        else:
            ans.append(str(node.data))
            q.append(node.left)
            q.append(node.right)

    while ans and ans[-1] == "null":
        ans.pop()

    print("[" + ",".join(ans) + "]")

def getSuccessor(node):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def delNode(root,key):
    if root is None:
        return root
    if root.data > key:
        root.left = delNode(root.left, key)
    elif root.data < key:
        root.right = delNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        succ = getSuccessor(root)
        root.data = succ.data   
        root.right = delNode(root.right, succ.data)
    return root

if __name__ == "__main__":

    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)
    
    key = 7
    root = delNode(root, key)
    print(printTree(root))