m ,n = map(int,input().split())
k = int(input())
adj = [[] for _ in range(m)]

for i in range(m):
    adj[i] =list(map(int,input().split()))
    adj[i].pop(0)
    for j in range(len(adj[i])):
        adj[i][j] -= 1

def max_matching(m,n,adj):
    matching = [-1] * n
    num = 0

    def kuhn(u,visited):
        if visited[u]:
            return False
        visited[u] = True
        for nbr in adj[u] :
            if matching[nbr] == -1 or kuhn(matching[nbr],visited):
                matching[nbr] = u
                return True
        return False
    for u in range(m):
        visited = [False] * m
        if kuhn(u,visited):
            num += 1
    return num
print(max_matching(m,n,adj))