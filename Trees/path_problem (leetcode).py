class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(self, root):
    result = []
    path = []
    
    def dfs(node):
        if node is None:
            return

        path.append(str(node.val))

        if node.left is None and node.right is None:
            result.append("->".join(path))
        else:
            dfs(node.left)
            dfs(node.right)
        path.pop()

    dfs(root)
    
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    paths = binaryTreePaths(None, root)
    print(paths)  