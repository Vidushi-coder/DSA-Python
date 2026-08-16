from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def insert(root,key):
    temp = Node(key)

    if root is None:
        return temp

    curr = root
    while curr is not None:
        if curr.data < key and curr.right is not None:
            curr = curr.right
        elif curr.data > key and curr.left is not None:
            curr = curr.left
        else:
            break

    if curr.data < key:
        curr.right = temp
    else:
        curr.left = temp

    return root

def printTree(root):
    if root is None:
        return ("[]")

    ans = []
    q = deque([root])

    while q:
        curr = q.popleft()

        if curr is None:
            ans.append("Null")
        else:
            ans.append(str(curr.data))
            q.append(curr.left)
            q.append(curr.right)

    while ans and ans[-1]=="Null":
        ans.pop()

    print("["+",".join(ans)+"]")

if __name__ == "__main__":
    root = Node(22)
    root.left = Node(12)
    root.right = Node(30)
    root.left.left = Node(8)
    root.left.right = Node(20)
    root.left.right.right = Node(21)

    key = 15

    root = insert(root,key)

    printTree(root)