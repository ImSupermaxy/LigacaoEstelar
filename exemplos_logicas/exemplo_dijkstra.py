import heapq

def dijkstra(grafo, inicio, destino):
    fila = [(0, inicio, [inicio])]  # (custo_acumulado, nó_atual, caminho)
    visitado = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)

        if atual == destino:
            return caminho, custo  # Caminho e custo total

        if atual in visitado:
            continue
        visitado.add(atual)

        for vizinho, peso in grafo[atual]:
            if vizinho not in visitado:
                heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))

    return None, float('inf')  # Caso não encontre caminho

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

caminho, custo = dijkstra(grafo, 'A', 'F')
print(f'Caminho: {caminho}, Custo: {custo}')
# Saída esperada: Caminho mais curto com menor custo
