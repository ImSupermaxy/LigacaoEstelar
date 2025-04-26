import heapq

def prim(grafo, inicio):
    visitado = set()
    mst = []
    heap = []

    # Adiciona todas as arestas do nó inicial ao heap
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(heap, (peso, inicio, vizinho))

    visitado.add(inicio)

    while heap:
        peso, u, v = heapq.heappop(heap)

        if v not in visitado:
            visitado.add(v)
            mst.append((u, v, peso))

            for vizinho, peso_v in grafo[v]:
                if vizinho not in visitado:
                    heapq.heappush(heap, (peso_v, v, vizinho))

    return mst

grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1), ('E', 2)],
    'E': [('D', 2)]
}

mst = prim(grafo, 'A')
for u, v, peso in mst:
    print(f"{u} - {v}: {peso}")


# Saída esperada:
# A - B: 1
# B - C: 1
# C - D: 1
# D - E: 2