class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inverted_root = invert_tree(root)

    print(inverted_root.value)  
    print(inverted_root.left.value)  
    print(inverted_root.right.value)  
    print(inverted_root.right.left.value)  
    print(inverted_root.right.right.value)  