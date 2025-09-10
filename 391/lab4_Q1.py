import heapq
from collections import defaultdict

class Solution():
    def dijkstra(self, adj, src=1):
        pq = []
        pq.append((0, src, [])) # path length, node, current_path
        distances = {}
        shortestPaths = defaultdict(list)

        while pq:
            path_len, node, cur_path = heapq.heappop(pq)
            if node in distances and path_len > distances[node]:
                continue
            distances[node] = path_len
            new_path = cur_path.copy()
            new_path.append(node)
            shortestPaths[node].append(new_path)

            for nei, weight in adj[node]:
                heapq.heappush(pq, (weight + path_len, nei, new_path))

        return distances, shortestPaths
    
if __name__ == "__main__":
    nodes, edges = list(map(int, input().split(" ")))
    adj = {node: [] for node in range(1, nodes+1)}
    for _ in range(edges):
        n1, n2, wt = list(map(int, input().split(" ")))
        adj[n1].append((n2, wt))
    s = Solution()
    src = 1
    distances, shortestPaths = s.dijkstra(adj, src)
    for i in range(1, nodes+1):
        print(f"Shortest Path from {src} to {i} is of length {distances[i]}. Possible paths: ", shortestPaths[i])