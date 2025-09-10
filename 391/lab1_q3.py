from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GraphNode:
    def __init__(self, val) -> None:
        self.val = val

def findDiameter(root: TreeNode):

    adj = defaultdict(list[GraphNode])
    
    def convertToGraph(node: TreeNode, graph_node: Optional[GraphNode] = None):
        if not graph_node:
            graph_node = GraphNode(node.val)

        if node.left:
            leftNode = GraphNode(node.left)
            adj[graph_node].append(leftNode)
            convertToGraph(node.left, leftNode)

        if node.right:
            rightNode = GraphNode(node.right)
            adj[graph_node].append(node.right)
            convertToGraph(node.right, rightNode)

    convertToGraph(root)

    X = list(adj.keys())[0]

    def bfs(node: GraphNode, path: int):
        
        q = deque()
        q.append(node)

        while q:
            for _ in range(len(q)):
                ele = q.popleft()
                if not adj[ele] and not q:
                    return ele, path
                
                for nei in adj[ele]:
                    q.append(nei)

    A, _ = bfs(X, 0)
    B, diameter = bfs(A, 0)

    return diameter