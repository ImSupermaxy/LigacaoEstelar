from collections import deque

def bfs(grafo, inicio, destino):
    visitado = set()
    fila = deque([(inicio, [inicio])])  # (nó_atual, caminho_para_chegar_aqui)

    while fila:
        atual, caminho = fila.popleft()

        if atual == destino:
            return caminho  # Encontrou o caminho mais curto

        visitado.add(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitado:
                fila.append((vizinho, caminho + [vizinho]))
                visitado.add(vizinho)

    return None  # Caminho não encontrado

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

caminho = bfs(grafo, 'A', 'F')
print(caminho)  # Exemplo de saída: ['A', 'C', 'F']
