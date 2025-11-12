from collections import deque, defaultdict

# Helper BFS to find augmenting path and flow
def bfs(s, t, adj, capacity):
    parent = [-1] * len(adj)
    parent[s] = -2  # mark source as visited
    q = deque([(s, float('inf'))])  # store (node, current_flow)

    while q:
        cur, flow = q.popleft()
        for nei in adj[cur]:
            # if neighbor not visited and has residual capacity
            if parent[nei] == -1 and capacity[cur][nei] > 0:
                parent[nei] = cur
                new_flow = min(flow, capacity[cur][nei])
                if nei == t:
                    return new_flow, parent  # found path to sink
                q.append((nei, new_flow))
    return 0, parent  # no augmenting path


# Edmonds-Karp Max Flow algorithm
def maxflow(adj, s, t, capacity):
    flow = 0
    while True:
        new_flow, parent = bfs(s, t, adj, capacity)
        if new_flow == 0:  # no more augmenting paths
            break
        flow += new_flow
        cur = t
        # update residual capacities along the path
        while cur != s:
            prev = parent[cur]
            capacity[prev][cur] -= new_flow
            capacity[cur][prev] += new_flow
            cur = prev
    return flow

# MAIN: Bipartite Matching using Max Flow
# Example Bipartite Graph:
# U = {1, 2, 3}
# V = {4, 5, 6}
# Edges = [(1,4), (1,5), (2,5), (2,6), (3,6)]

# Total vertices = source (0) + U + V + sink
U = [1, 2, 3]
V = [4, 5, 6]
s, t = 0, 7  # source = 0, sink = 7

# Initialize adjacency list and capacity matrix
adj = defaultdict(list)
capacity = [[0] * (t + 1) for _ in range(t + 1)]

# Connect source to all U vertices (capacity 1)
for u in U:
    adj[s].append(u)
    adj[u].append(s)
    capacity[s][u] = 1

# Connect all V vertices to sink (capacity 1)
for v in V:
    adj[v].append(t)
    adj[t].append(v)
    capacity[v][t] = 1

# Add bipartite edges (capacity 1)
edges = [(1,4), (1,5), (2,5), (2,6), (3,6)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
    capacity[u][v] = 1

# Compute maximum flow
flow_value = maxflow(adj, s, t, capacity)
print("Maximum Matching Size:", flow_value)

# Recover the matched pairs (U -> V)
matching = []
for u in U:
    for v in adj[u]:
        # If edge originally had capacity 1 and now has 0,
        # it means flow was sent (i.e., u is matched to v)
        if v in V and capacity[u][v] == 0:
            matching.append((u, v))

print("Matched pairs:", matching)
