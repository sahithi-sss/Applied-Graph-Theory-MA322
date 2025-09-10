import heapq

def bidirectional_dijkstra(n, edges, s, t):
    graph = [[] for _ in range(n+1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist_f, dist_r = [float('inf')] * (n+1), [float('inf')] * (n+1)
    parent_f, parent_r = [-1]*(n+1), [-1]*(n+1)

    dist_f[s], dist_r[t] = 0, 0
    Qf, Qr = [(0, s)], [(0, t)]
    visited_f, visited_r = set(), set()
    mu, meeting_node = float('inf'), -1

    while Qf and Qr:
        if Qf and (not Qr or Qf[0][0] <= Qr[0][0]):
            d, u = heapq.heappop(Qf)
            if u in visited_f: continue
            visited_f.add(u)
            if u in visited_r and dist_f[u] + dist_r[u] < mu:
                mu, meeting_node = dist_f[u] + dist_r[u], u
            for v, w in graph[u]:
                if dist_f[v] > dist_f[u] + w:
                    dist_f[v], parent_f[v] = dist_f[u] + w, u
                    heapq.heappush(Qf, (dist_f[v], v))
        else:
            d, u = heapq.heappop(Qr)
            if u in visited_r: continue
            visited_r.add(u)
            if u in visited_f and dist_f[u] + dist_r[u] < mu:
                mu, meeting_node = dist_f[u] + dist_r[u], u
            for v, w in graph[u]:
                if dist_r[v] > dist_r[u] + w:
                    dist_r[v], parent_r[v] = dist_r[u] + w, u
                    heapq.heappush(Qr, (dist_r[v], v))

        if Qf and Qr and Qf[0][0] + Qr[0][0] >= mu:
            break

    if mu == float('inf'):
        return None, []

    path = []
    u = meeting_node
    while u != -1:
        path.append(u)
        u = parent_f[u]
    path = path[::-1]   # forward path up to meeting_node

    u = parent_r[meeting_node]   # skip meeting_node here
    while u != -1:
        path.append(u)
        u = parent_r[u]

    return mu, path


# Example usage
n, m = 6, 7
edges = [(1,2,2),(1,3,4),(2,4,7),(3,4,1),(3,5,3),(4,6,1),(5,6,5)]
s, t = 1, 6
dist, path = bidirectional_dijkstra(n, edges, s, t)
print("Shortest distance from {} to {}: {}".format(s, t, dist))
print("Path:", " -> ".join(map(str, path)))
