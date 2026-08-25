class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_symmetric(root):
    if root is None:
        return True

    def symmetric(p,q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.value != q.value:
            return False

        return symmetric(p.left,q.right) and symmetric(p.right,q.left)

    return symmetric(root.left, root.right)

if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(is_symmetric(root))  