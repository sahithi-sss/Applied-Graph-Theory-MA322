from collections import deque
import copy

# Edmonds–Karp: BFS to find shortest augmenting path
def bfs(s, t, adj, capacity):
    parent = [-1] * len(adj)   # store parent to reconstruct path
    parent[s] = -2             # mark source as visited
    q = deque([(s, float('inf'))])  # (node, possible flow)

    while q:
        u, flow = q.popleft()
        for v in adj[u]:
            # proceed only if edge has capacity left and not visited
            if parent[v] == -1 and capacity[u][v] > 0:
                parent[v] = u
                new_flow = min(flow, capacity[u][v])
                if v == t:      # reached sink
                    return new_flow, parent
                q.append((v, new_flow))
    return 0, parent


# Main Edmonds–Karp Max Flow
def edmonds_karp(adj, s, t, capacity):
    flow = 0
    cap = copy.deepcopy(capacity)  # work on a copy of capacity

    while True:
        new_flow, parent = bfs(s, t, adj, cap)
        if new_flow == 0:          # no more augmenting paths
            break
        flow += new_flow

        # backtrack and update residual capacities
        cur = t
        while cur != s:
            prev = parent[cur]
            cap[prev][cur] -= new_flow
            cap[cur][prev] += new_flow
            cur = prev

    return flow, cap


# Find nodes reachable from s in the residual graph
def find_min_cut_set(s, adj, residual):
    visited = set()
    q = deque([s])
    while q:
        u = q.popleft()
        visited.add(u)
        for v in adj[u]:
            if v not in visited and residual[u][v] > 0:
                q.append(v)
    return visited


# Identify edges forming the minimum cut
def get_min_cut_edges(adj, capacity, residual, S):
    cut_edges = []
    for u in range(len(adj)):
        for v in adj[u]:
            # edge crosses from S to T and is saturated
            if u in S and v not in S and capacity[u][v] > 0:
                cut_edges.append((u, v))
    return cut_edges


# Check if min cut is unique
# (If residual graph has another minimal cut of same capacity)
def is_min_cut_unique(adj, capacity, s, t, flow_value):
    # We can test uniqueness by slightly reducing any min cut edge
    # and checking if max flow decreases (implying unique)
    # This is a simple heuristic check.
    for u in range(len(adj)):
        for v in adj[u]:
            if capacity[u][v] > 0:
                new_cap = copy.deepcopy(capacity)
                new_cap[u][v] -= 1e-6  # tiny reduction
                new_flow, _ = edmonds_karp(adj, s, t, new_cap)
                if abs(new_flow - flow_value) < 1e-6:
                    return False
    return True


# Example Graph
adj = {
    0: [1, 4],
    1: [2, 3],
    2: [5],
    3: [2, 5],
    4: [1, 3],
    5: []
}

capacity = [
    [0, 7, 0, 0, 4, 0],
    [0, 0, 5, 3, 0, 0],
    [0, 0, 0, 0, 0, 8],
    [0, 0, 3, 0, 0, 5],
    [0, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

s, t = 0, 5

# Compute max flow
max_flow_value, residual = edmonds_karp(adj, s, t, capacity)

# Find reachable nodes from s in residual graph
S = find_min_cut_set(s, adj, residual)
T = set(range(len(adj))) - S

# Get the edges forming the min cut
cut_edges = get_min_cut_edges(adj, capacity, residual, S)

# Check uniqueness (simple heuristic)
unique = is_min_cut_unique(adj, capacity, s, t, max_flow_value)

# Results
print(f"Maximum Flow: {max_flow_value}")
print(f"Minimum Cut edges: {cut_edges}")
print(f"Min Cut Partition: S = {S}, T = {T}")
print(f"Is Minimum Cut Unique? {'Yes' if unique else 'No'}")
