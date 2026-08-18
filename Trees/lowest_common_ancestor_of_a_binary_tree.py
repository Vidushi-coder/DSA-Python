class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root,p,q):
    if root is None:
        return None
    
    if root.data==p or root.data==q:
        return root
    
    left_lca = lca(root.left,p,q)
    right_lca = lca(root.right,p,q)

    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca

root = Node(3)
root.left = Node(5)
root.right = Node(1)    
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)  

p = 6
q = 2 

lca_node = lca(root, p, q)
if lca_node:    
    print("Lowest Common Ancestor of", p, "and", q, "is:", lca_node.data)