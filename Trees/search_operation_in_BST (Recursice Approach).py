class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left,key)
    return search(root.right,key)

root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(9)

key = 7
print(search(root, key))