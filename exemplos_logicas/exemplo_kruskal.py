class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def kruskal(vertices, arestas):
    mst = []
    uf = UnionFind(vertices)
    arestas.sort(key=lambda x: x[2])  # ordena por peso

    for u, v, peso in arestas:
        if uf.union(u, v):
            mst.append((u, v, peso))

    return mst


vertices = ['A', 'B', 'C', 'D', 'E']
arestas = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 1),
    ('D', 'E', 2)
]

mst = kruskal(vertices, arestas)
for u, v, peso in mst:
    print(f"{u} - {v}: {peso}")
