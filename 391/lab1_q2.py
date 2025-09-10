from collections import deque

def bfs(adj, start):

    q = deque()
    q.append(start)

    traversal = []
    visit = set()

    while q:
        for _ in range(len(q)):
            ele = q.popleft()

            visit.add(ele)
            traversal.append(ele)

            for nei in adj[ele]:
                if nei not in visit:
                    q.append(nei)

    return traversal

def dfs(adj, start):
    traversal = []
    visit = set()

    def helper(node):
        if node in visit:
            return
        
        visit.add(node)

        for nei in adj[node]:
            helper(nei)

        traversal.append(node)

    helper(start)