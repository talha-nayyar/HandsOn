import math
import heapq
from collections import defaultdict, deque

# ------------- Core data structure -------------
class Graph:
    """Weighted directed (or undirected) graph using adjacency lists."""
    def __init__(self, directed: bool = True):
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    @property
    def vertices(self):
        verts = set(self.adj.keys())
        for u in self.adj:
            for v, _ in self.adj[u]:
                verts.add(v)
        return verts


# ------------- 1. Dijkstra (non-negative) -------------
def dijkstra(G: Graph, src):
    dist = {v: math.inf for v in G.vertices}
    pred = {v: None for v in G.vertices}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in G.adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, pred


# ------------- 2. Bellman-Ford (neg edges OK) -------------
def bellman_ford(G: Graph, src):
    verts = list(G.vertices)
    dist = {v: math.inf for v in verts}
    pred = {v: None for v in verts}
    dist[src] = 0

    # |V|-1 relaxation passes
    for _ in range(len(verts) - 1):
        updated = False
        for u in G.adj:
            for v, w in G.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    updated = True
        if not updated:
            break

    # detect negative cycle
    for u in G.adj:
        for v, w in G.adj[u]:
            if dist[u] + w < dist[v]:
                return None, None, True
    return dist, pred, False


# ------------- 3. Floyd-Warshall (all-pairs) -------------
def floyd_warshall(weights: dict):
    vs = list(weights.keys())
    dist = {i: {j: weights[i].get(j, math.inf) for j in vs} for i in vs}
    for v in vs:
        dist[v][v] = 0
    for k in vs:
        for i in vs:
            dik = dist[i][k]
            if dik == math.inf:
                continue
            for j in vs:
                if dik + dist[k][j] < dist[i][j]:
                    dist[i][j] = dik + dist[k][j]
    return dist


# ------------------- Test helpers -------------------
def assert_equal(a, b, msg=""):
    assert a == b, f"Assertion failed: {msg} Expected {b}, got {a}"

def assert_dist_dict(dd, expected):
    for k, v in expected.items():
        assert math.isclose(dd[k], v, rel_tol=0, abs_tol=1e-9), \
            f"Distance to {k} incorrect: expected {v}, got {dd[k]}"

# ------------------- Build CLRS graphs -------------------
def build_clrs_dijkstra_graph():
    g = Graph()
    for u, v, w in [
        ('s', 't', 10), ('s', 'y', 5), ('t', 'x', 1), ('t', 'y', 2),
        ('x', 'z', 4), ('y', 't', 3), ('y', 'x', 9), ('y', 'z', 2),
        ('z', 's', 7), ('z', 'x', 6)
    ]:
        g.add_edge(u, v, w)
    return g

def build_clrs_bf_graph():
    g = Graph()
    for u, v, w in [
        ('s', 't', 6), ('s', 'y', 7), ('t', 'x', 5), ('t', 'y', 8),
        ('t', 'z', -4), ('y', 'x', -3), ('y', 'z', 9), ('x', 't', -2),
        ('z', 'x', 7), ('z', 's', 2)
    ]:
        g.add_edge(u, v, w)
    return g

def build_clrs_fw_matrix():
    verts = [1,2,3,4]
    W = {i: {} for i in verts}
    for u, v, w in [(1,2,3),(1,3,8),(2,3,2),(3,4,1),(4,1,2)]:
        W[u][v] = w
    return W

# ------------------- Run tests -------------------
def run_tests():
    # Dijkstra
    g_dij = build_clrs_dijkstra_graph()
    dist_dij, _ = dijkstra(g_dij, 's')
    expected_dij = {'s':0, 't':8, 'x':9, 'y':5, 'z':7}
    assert_dist_dict(dist_dij, expected_dij)
    print("Dijkstra test: PASS")

    # Bellman-Ford
    g_bf = build_clrs_bf_graph()
    dist_bf, _, neg_cycle = bellman_ford(g_bf, 's')
    assert not neg_cycle, "Unexpected negative cycle"
    expected_bf = {'s':0, 't':2, 'x':4, 'y':7, 'z':-2}
    assert_dist_dict(dist_bf, expected_bf)
    print("Bellman-Ford test: PASS")

    # Floyd-Warshall
    W = build_clrs_fw_matrix()
    dist_fw = floyd_warshall(W)
    expected_fw = {
        1:{1:0,2:3,3:5,4:6},
        2:{1:5,2:0,3:2,4:3},
        3:{1:3,2:6,3:0,4:1},
        4:{1:2,2:5,3:7,4:0}
    }
    for i in expected_fw:
        for j in expected_fw[i]:
            assert math.isclose(dist_fw[i][j], expected_fw[i][j], abs_tol=1e-9), \
                f"FW dist({i},{j}) incorrect"
    print("Floyd-Warshall test: PASS")

run_tests()
