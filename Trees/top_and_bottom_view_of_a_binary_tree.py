# Top View

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def dfs(node,hd,level,topNodes):
    if node is None:
        return

    if hd not in topNodes or topNodes[hd][1] > level:
        topNodes[hd] = (node.data,level)

    dfs(node.left,hd-1,level+1,topNodes)
    dfs(node.right,hd+1,level+1,topNodes)

def topView(root):
    topNodes = {}
    dfs(root,0,0,topNodes)

    result = []
    if root is None:
        return result
    
    for hd in sorted(topNodes.keys()):
        result.append(topNodes[hd][0])

    return result

if __name__ == "__main__":

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    root.right.left = Node(90)
    root.right.right = Node(100)

    result = topView(root)
    print(" ".join(map(str, result)))

# Top View

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def dfs(node,hd,level,bottomNodes):
    if node is None:
        return

    if hd not in bottomNodes or bottomNodes[hd][1] < level:
        bottomNodes[hd] = (node.data,level)

    dfs(node.left,hd-1,level+1,bottomNodes)
    dfs(node.right,hd+1,level+1,bottomNodes)

def bottomView(root):
    result = []

    if root is None:
        return result

    bottomNodes = {}
    dfs(root,0,0,bottomNodes)   

    for hd in sorted(bottomNodes.keys()):
        result.append(bottomNodes[hd][0])   

    return result

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    root.right.left = Node(90)
    root.right.right = Node(100)

    result = bottomView(root)
    print(" ".join(map(str, result)))