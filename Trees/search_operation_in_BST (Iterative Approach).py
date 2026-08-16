class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,key):
    present = False

    while root is not None:
        if root.data == key:
            present = True
            break
        elif key < root.data:
            root = root.left
        else:
            root = root.right

    return present

if __name__ == "__main__":

    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)
    
    key = 7
    print(search(root, key))