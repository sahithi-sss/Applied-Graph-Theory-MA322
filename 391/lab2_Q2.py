from collections import defaultdict

M, N = map(int, input().split(" "))
adj = defaultdict(list)

for _ in range(N):
    u, v = map(int, input().split(" "))
    adj[u].append(v)
    adj[v].append(u)

def dfs(n, visit):

    if n in visit:
        return True, visit + [n]
    
    visit.append(n)
    
    for nei in adj[n]:
        if len(visit) < 2 or (len(visit) >= 2 and nei != visit[-2]):
            out = dfs(nei, visit)
            if out[0]:
                return True, out[1]

    visit.pop()
    return False, None

isCycle, path = False, None

for n in range(1, M+1):
    c, p = dfs(n, [])
    if c:
        isCycle, path = True, p
        break

if isCycle:
    print(path)
else:
    print("No")