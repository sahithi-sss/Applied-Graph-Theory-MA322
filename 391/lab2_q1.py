from collections import defaultdict

M, N = map(int, input().split(" "))
friends = {}

for _ in range(N):
    u, v = map(int, input().split(" "))
    friends[u] = v

adj = defaultdict(set)

for i in range(1, M+1):
    for j in range(i+1, M+1):
        adj[i].add(j)
        adj[j].add(i)

for u, v in friends.items():
    adj[u].remove(v)
    adj[v].remove(u)

def findConnectedComponents(adj):
    visit = set()
    n = 0

    for node in adj:
        if node not in visit:
            n += 1
            visit.add(node)
            for nei in list(adj[node]):
                visit.add(nei)

    return n

if findConnectedComponents(adj) == 2:
    print("Yes")
else:
    print("No")