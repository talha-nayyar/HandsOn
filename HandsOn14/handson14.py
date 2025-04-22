from collections import defaultdict, deque

def topological_sort(edges):
    """
    Kahn’s algorithm.
    edges: iterable of (u, v) tuples for directed edge u -> v
    returns: list representing one valid topological ordering
    """
    adj = defaultdict(list)
    indeg = defaultdict(int)

    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
        indeg.setdefault(u, 0)

    queue = deque([v for v, d in indeg.items() if d == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(order) != len(indeg):
        raise ValueError("Graph is not a DAG.")
    return order


def depth_first_search(graph):
    """
    Classic DFS for a directed graph.

    graph: dict {vertex: [adjacent vertices]}
    returns: discovery_times, finishing_times, parents, finished_order
    """
    time = 0
    color = {}
    d_time, f_time, parent = {}, {}, {}
    finished = []

    def visit(u):
        nonlocal time
        color[u] = "gray"
        time += 1
        d_time[u] = time
        for v in graph[u]:
            if color.get(v, "white") == "white":
                parent[v] = u
                visit(v)
        color[u] = "black"
        time += 1
        f_time[u] = time
        finished.append(u)

    for u in graph:
        if color.get(u, "white") == "white":
            parent[u] = None
            visit(u)

    return d_time, f_time, parent, finished


class DisjointSet:
    """Union‑Find with path compression + union by rank"""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        # union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        return True


def kruskal(nodes, weighted_edges):
    """
    Kruskal’s minimum‑spanning‑tree algorithm.

    nodes: iterable of vertex names
    weighted_edges: iterable of (weight, u, v) tuples
    returns: mst_edges (u,v,w) list, total_weight
    """
    ds = DisjointSet()
    for n in nodes:
        ds.make_set(n)

    mst, total = [], 0
    for w, u, v in sorted(weighted_edges):
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


# ---------- Example Graphs from CLRS (3rd ed.) ---------- #
# 1. Topological Sort (Figure 22‑4 “Laundry” DAG)
ts_edges = [
    ("undershorts", "pants"),
    ("undershorts", "shoes"),
    ("socks", "shoes"),
    ("pants", "belt"),
    ("pants", "shoes"),
    ("shirt", "tie"),
    ("shirt", "belt"),
    ("tie", "jacket"),
    ("belt", "jacket"),
]  # “watch” is isolated

# 2. Depth‑First Search (Figure 22‑5)
dfs_graph = {
    "u": ["v", "x"],
    "v": ["y"],
    "w": ["y", "z"],
    "x": ["v"],
    "y": ["x"],
    "z": ["z"],  # self‑loop to illustrate back‑edge
}

# 3. Kruskal MST example (Figure 23‑4)
nodes_kruskal = list("abcdefghi")
weighted_edges_kruskal = [
    (4, "a", "b"),
    (8, "a", "h"),
    (11, "b", "h"),
    (8, "b", "c"),
    (7, "c", "d"),
    (4, "c", "f"),
    (2, "c", "i"),
    (9, "d", "e"),
    (14, "d", "f"),
    (10, "e", "f"),
    (2, "f", "g"),
    (1, "g", "h"),
    (6, "g", "i"),
    (7, "h", "i"),
]

# ---------- Run Tests ---------- #
print("Topological sort order:")
print(topological_sort(ts_edges))

print("\nDFS discovery & finishing times:")
d_times, f_times, parents, finished = depth_first_search(dfs_graph)
for v in sorted(dfs_graph.keys()):
    print(f"{v}: d={d_times[v]}, f={f_times[v]}, parent={parents[v]}")
print("Finish stack (topological by finish time):", finished)

print("\nKruskal MST edges and total weight:")
mst_edges, mst_weight = kruskal(nodes_kruskal, weighted_edges_kruskal)
print("Edges in MST:", mst_edges)
print("Total weight:", mst_weight)