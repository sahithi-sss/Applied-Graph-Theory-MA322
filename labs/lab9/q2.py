import random
import heapq

# -----------------------------------------------------------
# Function: generate_random_graph
# Generates a random undirected graph with n vertices.
# Each edge (i, j) is included independently with probability = edge_prob.
# Returns:
#   graph : adjacency list representation
#   edges : list of all edges (i, j)
# -----------------------------------------------------------
def generate_random_graph(n, edge_prob=0.5):
    graph = {i: [] for i in range(n)}
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                graph[i].append(j)
                graph[j].append(i)
                edges.append((i, j))
    return graph, edges


# -----------------------------------------------------------
# Algorithm 1: Maximal Matching-based 2-Approximation
# Greedy approach:
#   - Initialize an empty vertex cover.
#   - Go through all edges.
#   - If both endpoints are uncovered, add both to the cover.
# Guarantees: produces a valid vertex cover of size ≤ 2 × OPT.
# -----------------------------------------------------------
def two_approximation(edges):
    vertex_cover = set()          # vertices chosen for cover
    unmatched = edges.copy()      # remaining edges to process

    while unmatched:
        u, v = unmatched.pop()    # take an arbitrary edge
        if u not in vertex_cover and v not in vertex_cover:
            vertex_cover.add(u)
            vertex_cover.add(v)
    return vertex_cover


# -----------------------------------------------------------
# Algorithm 2: Greedy Degree Heuristic
# Greedy approach:
#   - Repeatedly pick vertex with the maximum degree.
#   - Add it to vertex cover.
#   - Remove it and all its incident edges from the graph.
#
# Implementation details:
#   - Use a max-heap (negative degrees for heapq).
#   - Update degrees dynamically as edges are removed.
# -----------------------------------------------------------
def greedy_degree(graph):
    # Track whether a vertex has been removed
    removed = {v: False for v in graph}
    cover = set()

    # Compute initial degrees
    degrees = {v: len(graph[v]) for v in graph}

    # Initialize max-heap using (-degree, vertex)
    heap = [(-deg, v) for v, deg in degrees.items()]
    heapq.heapify(heap)

    while heap:
        neg_deg, u = heapq.heappop(heap)
        if removed[u]:
            continue  # skip if already removed
        if degrees[u] == 0:
            continue  # skip isolated vertex

        # Add vertex with maximum degree to cover
        cover.add(u)
        removed[u] = True

        # Remove all edges incident to u
        for v in graph[u]:
            if not removed[v]:
                degrees[v] -= 1  # update degree
        # Rebuild heap to reflect updated degrees
        heap = [(-degrees[v], v) for v in graph if not removed[v]]
        heapq.heapify(heap)

    return cover


# -----------------------------------------------------------
# Driver Code: Compare both algorithms on a random graph
# -----------------------------------------------------------
n = 6
g, e = generate_random_graph(n, edge_prob=0.5)

print("Graph adjacency list:")
for k, v in g.items():
    print(f"{k}: {v}")

print("\nEdges:", e)

# Run Algorithm 1 (2-Approximation)
vc1 = two_approximation(edges=e)
print("\n2-Approximation Vertex Cover:", vc1)
print("Size:", len(vc1))

# Run Algorithm 2 (Greedy Degree Heuristic)
vc2 = greedy_degree(g)
print("\nGreedy Degree Vertex Cover:", vc2)
print("Size:", len(vc2))
