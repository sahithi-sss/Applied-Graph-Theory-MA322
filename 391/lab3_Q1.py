class Solution:
    def areIsomorphicUnrooted(self, tree1, tree2):
        r1 = self.getRoots(tree1)
        r2 = self.getRoots(tree1)
        
        if len(r1) != len(r2):
            return False
        
        labels1 = [self.canonicalForm(self.rootTree(tree1, r)) for r in r1]
        labels2 = [self.canonicalForm(self.rootTree(tree2, r)) for r in r2]

        return any(l1 == l2 for l1 in labels1 for l2 in labels2)
    
    
    def rootTree(self, tree, root):
        rooted = {}
        def dfs(node):
            rooted[node] = []
            for neighbor in tree[node]:
                rooted[node].append(neighbor)
                dfs(neighbor)
        dfs(root)
        return rooted

    def canonicalForm(self, rooted):
        def encode(node):
            if not rooted[node]:
                return "()"
            labels = [encode(child) for child in rooted[node]]
            labels.sort()
            return "(" + "".join(labels) + ")"

        root = next(iter(rooted))
        return encode(root) 

    def getRoots(self, t):
        tree = {k: v[:] for k, v in t.items()}

        while len(tree) > 2:
            leaves = [node for node, children in tree.items() if not children]

            if not leaves:
                break
            
            for leaf in leaves:
                del tree[leaf]

            for node in tree:
                tree[node] = [child for child in tree[node] if child not in leaves]

        return list(tree)
    
tree1 = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: [6, 7],
    6: [],
    7: []
}


tree2 = {
    0: [2, 1],
    1: [4, 3],
    2: [],
    3: [],
    4: [],
    5: [7, 6],
    6: [5],
    7: []
}

isIso = (Solution().areIsomorphicUnrooted(tree1, tree2))
print(isIso)



