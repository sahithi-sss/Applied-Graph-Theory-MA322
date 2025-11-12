m, n = map(int, input().split())
e = int(input())

adj = [[] for _ in range(m)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)

def min_vertex_cover(m, n, adj):
    matching = [-1] * n    

    def kuhn(u, visited):
        if visited[u]:
            return False
        visited[u] = True
        for nbr in adj[u]:
            if matching[nbr] == -1 or kuhn(matching[nbr], visited):
                matching[nbr] = u
                return True
        return False
    
    # Step 1: Maximum matching
    for u in range(m):
        visited = [False] * m
        kuhn(u, visited)

    visited_A = [False] * m
    visited_B = [False] * n

    def dfs_A(u):
        visited_A[u] = True
        for v in adj[u]:
            # Traverse UNMATCHED edge (u,v)
            if not visited_B[v]:
                if matching[v] != u:  # edge not part of matching
                    visited_B[v] = True
                    # If v is matched, go to that A-vertex
                    if matching[v] != -1:
                        dfs_A(matching[v])


    # Step 2: Start DFS from unmatched vertices in A
    matched_A = [False] * m
    for v in range(n):
        if matching[v] != -1:
            matched_A[matching[v]] = True
    
    for u in range(m):
        if not matched_A[u]:
            dfs_A(u)

    # Step 3: König’s theorem ⇒
    cover_A = [u for u in range(m) if not visited_A[u]]
    cover_B = [v for v in range(n) if visited_B[v]]

    return cover_A, cover_B
        
cover_A, cover_B = min_vertex_cover(m, n, adj)
print("A:", *cover_A)
print("B:", *cover_B)
